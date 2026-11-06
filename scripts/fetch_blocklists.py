# -*- coding: utf-8 -*-
"""抓取 NextDNS 目录中的 51 个广告/跟踪器拦截列表，并提取所有被拦截的域名。

输出:
  blocklists/raw/<slug>__<file>        原始下载文件
  blocklists/domains/<slug>.txt        每个列表提取出的去重域名
  blocklists/ALL-domains-unique.txt    全部列表合并去重后的域名
  blocklists/REPORT.md                 抓取报告
"""
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(ROOT, "blocklists", "raw")
DOM_DIR = os.path.join(ROOT, "blocklists", "domains")
REPORT = os.path.join(ROOT, "blocklists", "REPORT.md")
ALL_DOM = os.path.join(ROOT, "blocklists", "ALL-domains-unique.txt")
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(DOM_DIR, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# 域名校验：至少一个点 + 字母 TLD，允许下划线/连字符，总长 <= 253
DOMAIN_RE = re.compile(r"^(?=.{1,253}$)([a-z0-9_]([a-z0-9_-]{0,61}[a-z0-9_])?\.)+[a-z]{2,63}$", re.I)
HOSTS_RE = re.compile(r"^(?:0\.0\.0\.0|127\.0\.0\.1|::1|::)\s+([^\s#]+)", re.I)
# ||domain^ / ||domain$opts / ||domain^| —— 带路径(/)的规则不提取，避免过度拦截
ABP_RE = re.compile(r"^\|\|([a-z0-9_.\-]+)\^?(?:\$|\||$)", re.I)
URL_ANCH_RE = re.compile(r"^\|[a-z0-9]+://([^/$*?^'\"\\]+)")


def out(*a):
    print(*a, flush=True)


def extract_domain(line, csv_mode=False):
    s = line.strip()
    if not s:
        return None
    if csv_mode:
        for field in s.split(","):
            field = field.strip().strip('"').lower()
            if field and DOMAIN_RE.match(field):
                return field
        return None
    c = s[0]
    if c in "!#;[":
        return None
    if s.startswith("@@"):  # 例外(白名单)规则，不算拦截
        return None
    m = HOSTS_RE.match(s)
    if m:
        d = m.group(1).lower().strip(".")
        return d if DOMAIN_RE.match(d) else None
    if "##" in s or "#@#" in s or "#$#" in s or "#?#" in s:  # 元素隐藏规则
        return None
    if s.startswith("*."):
        d = s[2:].split()[0].strip().strip(".").lower()
        return d if DOMAIN_RE.match(d) else None
    m = ABP_RE.match(s)
    if m:
        d = m.group(1).strip(".").lower()
        return d if DOMAIN_RE.match(d) else None
    if c == "|":  # |http://... 锚定 URL 规则
        m = URL_ANCH_RE.match(s.lower())
        if m:
            d = m.group(1).split(":")[0].strip(".").lower()
            if d.startswith("*."):
                d = d[2:]
            return d if DOMAIN_RE.match(d) else None
        return None
    tok = s.split()[0]
    tok = tok.split("$", 1)[0].split("/", 1)[0]
    tok = tok.strip().strip("^").strip(".").lower()
    if tok.startswith("*."):
        tok = tok[2:].strip()
    return tok if DOMAIN_RE.match(tok) else None


def fetch_file(urls, timeout=240):
    """按候选顺序尝试下载，返回 (data, url_used)。"""
    errs = []
    for url in urls:
        for _attempt in range(2):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return r.read(), url
            except urllib.error.HTTPError as e:
                errs.append(f"{url} -> HTTP {e.code}")
                if e.code in (400, 401, 403, 404, 405, 406, 410, 451):
                    break
                time.sleep(2)
            except Exception as e:
                errs.append(f"{url} -> {type(e).__name__}: {e}")
                time.sleep(2)
        if any("CERTIFICATE_VERIFY_FAILED" in x or "SSLError" in x for x in errs[-2:]):
            try:
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
                    return r.read(), url + "（证书校验已跳过）"
            except Exception as e:
                errs.append(f"{url} -> SSL fallback: {type(e).__name__}: {e}")
    raise RuntimeError(" | ".join(errs[-6:]))


def gh(repo, branch, path):
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{path}"


def build_sources():
    # NextDNS 原生列表: nextdns/native-tracking-domains 仓库已删除(404)，官方未再公开发布，
    # 保留原路径重试，失败则如实记录为"已下架"。
    def NG(f):
        return [gh("nextdns/native-tracking-domains", b, f"domains/{f}") for b in ("master", "main")]
    def AG(paths):
        return [{"urls": [gh("AdguardTeam/AdguardFilters", "master", p)]} for p in paths]
    def HZ(level):
        # 仓库已改版: 纯域名版在 wildcard/<level>-onlydomains.txt，通配符版在 wildcard/<level>.txt
        # 注意: normal 级别的文件名为 multi
        return [{"urls": [gh("hagezi/dns-blocklists", "main", f"wildcard/{level}.txt")]},
                {"urls": [gh("hagezi/dns-blocklists", "main", f"wildcard/{level}-onlydomains.txt")]}]

    return [
        {"idx": 1, "slug": "nextdns-ads-trackers", "title": "NextDNS 广告和跟踪器拦截列表", "expected": 79006,
         "files": [{"urls": NG("ads--trackers")}]},
        {"idx": 2, "slug": "nextdns-youtube-ads", "title": "NextDNS YouTube 广告拦截", "expected": 2,
         "files": [{"urls": NG("youtube-ads")}]},
        {"idx": 3, "slug": "adguard-dns", "title": "AdGuard DNS filter", "expected": 189177,
         "files": [{"urls": [gh("AdguardTeam/AdguardSDNSFilter", "master", "Filters/adguard_dns_filter.txt"),
                             "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"]}]},
        {"idx": 4, "slug": "oisd", "title": "OISD", "expected": 232695,
         "files": [{"urls": ["https://big.oisd.nl/domainswild"]},
                   {"urls": ["https://small.oisd.nl/domainswild"]}]},
        {"idx": 5, "slug": "adguard-mobile", "title": "AdGuard Mobile Ads filter", "expected": 952,
         "files": AG(["MobileFilter/sections/adservers.txt", "MobileFilter/sections/specific_app.txt",
                      "MobileFilter/sections/specific_web.txt"])},
        {"idx": 6, "slug": "nextdns-reddit-ads", "title": "NextDNS Reddit 广告拦截", "expected": 3,
         "files": [{"urls": NG("reddit-ads")}]},
        {"idx": 7, "slug": "adguard-tracking", "title": "AdGuard Tracking Protection filter", "expected": 119138,
         "files": AG(["SpywareFilter/sections/tracking_servers.txt", "SpywareFilter/sections/tracking_servers_firstparty.txt",
                      "SpywareFilter/sections/mobile.txt", "SpywareFilter/sections/specific.txt",
                      "SpywareFilter/sections/general_url.txt"])},
        {"idx": 8, "slug": "goodbyeads", "title": "Goodbye Ads", "expected": 277778,
         "files": [{"urls": [gh("jerryn70/GoodbyeAds", "master", "Formats/GoodbyeAds-AdBlock-Filter.txt")]},
                   {"urls": [gh("jerryn70/GoodbyeAds", "master", "Formats/GoodbyeAds-Ultra-AdBlock-Filter.txt")]},
                   {"urls": [gh("jerryn70/GoodbyeAds", "master", "Formats/GoodbyeAds-YouTube-AdBlock-Filter.txt")]}]},
        {"idx": 9, "slug": "easylist", "title": "EasyList", "expected": 46893,
         "files": [{"urls": ["https://easylist.to/easylist/easylist.txt",
                             gh("easylist/easylist", "master", "easylist.txt")]}]},
        {"idx": 10, "slug": "hagezi-proplus", "title": "HaGeZi - Multi PRO++", "expected": 238296,
         "files": HZ("pro.plus")},
        {"idx": 11, "slug": "adguard-base", "title": "AdGuard Base filter", "expected": 59460,
         "files": AG(["BaseFilter/sections/adservers.txt", "BaseFilter/sections/adservers_firstparty.txt",
                      "BaseFilter/sections/specific.txt", "BaseFilter/sections/general_url.txt",
                      "BaseFilter/sections/cryptominers.txt", "BaseFilter/sections/foreign.txt"])},
        {"idx": 12, "slug": "hagezi-pro", "title": "HaGeZi - Multi PRO", "expected": 222630,
         "files": HZ("pro")},
        {"idx": 13, "slug": "stevenblack", "title": "Steven Black", "expected": 77769,
         "files": [{"urls": [gh("StevenBlack/hosts", "master", "hosts")]}]},
        {"idx": 14, "slug": "easyprivacy", "title": "EasyPrivacy", "expected": 47126,
         "files": [{"urls": ["https://easylist.to/easylist/easyprivacy.txt",
                             gh("easylist/easylist", "master", "easyprivacy.txt")]}]},
        {"idx": 15, "slug": "hagezi-normal", "title": "HaGeZi - Multi NORMAL", "expected": 178087,
         "files": HZ("multi")},
        {"idx": 16, "slug": "fanboy-annoyance", "title": "Fanboy's Annoyance List", "expected": 920,
         "files": [{"urls": ["https://easylist.to/easylist/fanboy-annoyance.txt",
                             gh("easylist/easylist", "master", "fanboy-annoyance.txt")]}]},
        {"idx": 17, "slug": "hagezi-ultimate", "title": "HaGeZi - Multi ULTIMATE", "expected": 273572,
         "files": HZ("ultimate")},
        {"idx": 18, "slug": "adaway", "title": "AdAway", "expected": 6541,
         "files": [{"urls": [gh("AdAway/adaway.github.io", "master", "hosts.txt")]}]},
        {"idx": 19, "slug": "disconnect-ads", "title": "Disconnect (Ads)", "expected": 2700,
         "files": [{"urls": ["https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt"]}]},
        {"idx": 20, "slug": "adguard-social", "title": "AdGuard Social Media filter", "expected": 48,
         "files": AG(["SocialFilter/sections/social_trackers.txt", "SocialFilter/sections/popups.txt"])},
        {"idx": 21, "slug": "adguard-russian", "title": "AdGuard Russian filter", "expected": 1965,
         "files": AG(["CyrillicFilters/common-sections/adservers.txt",
                      "CyrillicFilters/common-sections/adservers_firstparty.txt",
                      "CyrillicFilters/common-sections/general_url.txt",
                      "CyrillicFilters/common-sections/specific.txt",
                      "CyrillicFilters/RussianFilter/sections/adservers_firstparty.txt",
                      "CyrillicFilters/RussianFilter/sections/specific.txt"])},
        {"idx": 22, "slug": "dan-pollock", "title": "someonewhocares.org (Dan Pollock)", "expected": 12983,
         "files": [{"urls": ["https://someonewhocares.org/hosts/zero/hosts",
                             "http://someonewhocares.org/hosts/zero/hosts"]}]},
        {"idx": 23, "slug": "hblock", "title": "hBlock", "expected": 478220,
         "files": [{"urls": ["https://hblock.molinero.dev/hosts",
                             "https://hblock.molinero.dev/hosts_unified"]}]},
        {"idx": 24, "slug": "shadowwhisperer", "title": "ShadowWhisperer Tracking", "expected": 121085,
         "files": [{"urls": [gh("ShadowWhisperer/BlockLists", "master", "Lists/Tracking")]}]},
        {"idx": 25, "slug": "easylist-lithuania", "title": "EasyList Lithuania", "expected": 32,
         "files": [{"urls": [gh("EasyList-Lithuania/easylist_lithuania", b, "easylistlithuania.txt")
                             for b in ("master", "main")]},
                   {"urls": [gh("EasyList-Lithuania/easylist_lithuania", b, "EasyListLithuaniaHosts.txt")
                             for b in ("master", "main")]}]},
        {"idx": 26, "slug": "hufilter", "title": "hufilter", "expected": 92,
         "files": [{"urls": [gh("hufilter/hufilter", b, f"sections/{n}") for b in ("master", "main")]}
                   for n in ("ads.txt", "trackers.txt", "security.txt", "selfpromo.txt",
                             "annoyances.txt", "antiadblock.txt")]},
        {"idx": 27, "slug": "latvian-list", "title": "Latvian List", "expected": 40,
         "files": [{"urls": [gh("Latvian-List/adblock-latvian", b, p) for b in ("master", "main")
                             for p in ("lists/latvian-list.txt", "latvian-list.txt")]}]},
        {"idx": 28, "slug": "easylist-czsk", "title": "EasyList Czech and Slovak", "expected": 93,
         "files": [{"urls": [gh("tomasko126/easylistczechandslovak", b, "filters.txt") for b in ("master", "main")]}]},
        {"idx": 29, "slug": "turk-adlist", "title": "bkrucarci turk-adlist", "expected": 1214,
         "files": [{"urls": [gh("bkrucarci/turk-adlist", b, f) for b in ("master", "main")
                             for f in ("hosts", "turk-adlist.txt")]}]},
        {"idx": 30, "slug": "frellwit-swedish", "title": "Frellwit's Swedish Hosts File", "expected": 1152,
         "files": [{"urls": [gh("lassekongo83/Frellwits-filter-lists", b, "Frellwits-Swedish-Hosts-File.txt")
                             for b in ("master", "main")]}]},
        {"idx": 31, "slug": "ad-wars", "title": "ad-wars", "expected": 1646,
         "files": [{"urls": [gh("jdlingyu/ad-wars", b, "hosts") for b in ("master", "main")]}]},
        {"idx": 32, "slug": "liste-ar", "title": "Liste AR", "expected": 73,
         "files": [{"urls": ["https://easylist-downloads.adblockplus.org/liste_ar.txt"]}]},
        {"idx": 33, "slug": "easylist-hebrew", "title": "EasyList Hebrew", "expected": 140,
         "files": [{"urls": [gh("easylist/EasyListHebrew", b, "EasyListHebrew.txt") for b in ("master", "main")]}]},
        {"idx": 34, "slug": "certyficateit", "title": "CertyficateIT (波兰)", "expected": 1142,
         "files": [{"urls": [gh("MajkiIT/polish-ads-filter", b, "polish-adblock-filters/adblock.txt")
                             for b in ("master", "main")]}]},
        {"idx": 35, "slug": "finnish-easylist", "title": "Finnish Easylist Addition", "expected": 15,
         "files": [{"urls": [gh("finnish-easylist-addition/finnish-easylist-addition", b, "Finland_adb.txt")
                             for b in ("master", "main")]},
                   {"urls": [gh("finnish-easylist-addition/finnish-easylist-addition", b, "Finland_adb_uBO_extras.txt")
                             for b in ("master", "main")]}]},
        {"idx": 36, "slug": "wally3k", "title": "Personal Blocklist by WaLLy3K", "expected": 351,
         "files": [{"urls": ["https://v.firebog.net/hosts/static/w3kbl.txt"]}]},
        {"idx": 37, "slug": "easylist-dutch", "title": "EasyList Dutch", "expected": 56,
         "files": [{"urls": ["https://easylist-downloads.adblockplus.org/easylistdutch.txt"]}]},
        {"idx": 38, "slug": "youslist", "title": "YousList (韩语)", "expected": 626,
         "files": [{"urls": [gh("yous/YousList", b, "youslist.txt") for b in ("master", "main")]}]},
        {"idx": 39, "slug": "easylist-italy", "title": "EasyList Italy", "expected": 93,
         "files": [{"urls": ["https://easylist-downloads.adblockplus.org/easylistitaly.txt"]}]},
        {"idx": 40, "slug": "abpindo", "title": "ABPindo (印尼/马来)", "expected": 125,
         "files": [{"urls": [gh("ABPindo/indonesianadblockrules", b, f"subscriptions/{n}")
                             for b in ("master", "main")]}
                   for n in ("abpindo.txt", "abpindo_hosts.txt", "domain.txt")]},
        {"idx": 41, "slug": "1hosts-lite", "title": "1Hosts (Lite)", "expected": 102259,
         "files": [{"urls": [gh("badmojr/1Hosts", b, f"Lite/{f}") for b in ("master", "main")
                             for f in ("domains.txt", "hosts.txt")]}]},
        {"idx": 42, "slug": "disconnect-malvertising", "title": "Disconnect (Malvertising)", "expected": 2736,
         "files": [{"urls": ["https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt"]}]},
        {"idx": 43, "slug": "ruadlist", "title": "RU AdList", "expected": 9088,
         "files": [{"urls": [gh("ruadlist/ruadlist", "master", "ruadlist.txt"),
                             "https://easylist-downloads.adblockplus.org/ruadlist.txt"]}]},
        {"idx": 44, "slug": "hagezi-light", "title": "HaGeZi - Multi LIGHT", "expected": 87809,
         "files": HZ("light")},
        {"idx": 45, "slug": "easylist-china", "title": "EasyList China", "expected": 5903,
         "files": [{"urls": ["https://easylist-downloads.adblockplus.org/easylistchina.txt",
                             gh("easylist/easylistchina", "master", "easylistchina.txt")]}]},
        {"idx": 46, "slug": "anudeep", "title": "Anudeep's Blacklist", "expected": 42358,
         "files": [{"urls": [gh("anudeepND/blacklist", b, "adservers.txt") for b in ("master", "main")]}]},
        {"idx": 47, "slug": "perflyst-smarttv", "title": "Perflyst's Smart-TV Blocklist", "expected": 498,
         "files": [{"urls": [gh("Perflyst/PiHoleBlocklist", b, f) for b in ("master", "main")
                             for f in ("SmartTV.txt", "smarttv.txt")]}]},
        {"idx": 48, "slug": "pgl-yoyo", "title": "Peter Lowe", "expected": 3559,
         "files": [{"urls": ["https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext"]}]},
        {"idx": 49, "slug": "anti-ad", "title": "anti-AD (中文)", "expected": 110042,
         "files": [{"urls": ["https://anti-ad.net/domains.txt",
                             gh("privacy-protection-tools/anti-AD", "master", "anti-ad-domains.txt")]}]},
        {"idx": 50, "slug": "disconnect-tracking", "title": "Disconnect (Tracking)", "expected": 34,
         "files": [{"urls": ["https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt"]}]},
        {"idx": 51, "slug": "notrack", "title": "NoTrack Tracker Blocklist", "expected": 15214,
         "files": [{"urls": [f"https://gitlab.com/quidsup/notrack-blocklists/-/raw/{b}/notrack-blocklist.txt"
                             for b in ("master", "main")]},
                   {"urls": [f"https://gitlab.com/quidsup/notrack-blocklists/-/raw/{b}/notrack-tracker.txt"
                             for b in ("master", "main")]}]},
    ]


def process_source(src):
    domains = set()
    files = []
    for f in src["files"]:
        entry = {"urls": f["urls"], "ok": False}
        try:
            data, url = fetch_file(f["urls"])
            entry["ok"] = True
            entry["url"] = url
            entry["bytes"] = len(data)
            base = url.split("://", 1)[-1].split("?")[0].rstrip("/").split("/")[-1] or "index"
            raw_path = os.path.join(RAW_DIR, f"{src['slug']}__{base}")
            with open(raw_path, "wb") as fh:
                fh.write(data)
            n_lines = 0
            for raw in data.split(b"\n"):
                n_lines += 1
                line = raw.decode("utf-8", errors="replace")
                d = extract_domain(line, f.get("csv", False))
                if d:
                    domains.add(d)
            entry["lines"] = n_lines
        except Exception as e:
            entry["error"] = f"{type(e).__name__}: {e}"
        files.append(entry)
    return src, domains, files


def fmt_bytes(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f}{unit}" if unit != "B" else f"{n}B"
        n /= 1024
    return f"{n:.1f}TB"


def main():
    t0 = time.time()
    sources = build_sources()
    out(f"共 {len(sources)} 个来源，开始并行抓取 (6 线程)...\n")

    union = set()
    results = {}
    done = 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(process_source, s) for s in sources]
        for fut in as_completed(futs):
            try:
                src, domains, files = fut.result()
            except Exception as e:
                out(f"[!] 线程异常: {e}")
                continue
            done += 1
            if domains:
                with open(os.path.join(DOM_DIR, src["slug"] + ".txt"), "w",
                          encoding="utf-8", newline="\n") as fh:
                    fh.write("\n".join(sorted(domains)) + "\n")
                union |= domains
            ok_files = [f for f in files if f.get("ok")]
            status = "✓" if domains else "✗ 失败"
            out(f"[{done:>2}/{len(sources)}] {status} {src['title']}: {len(domains):,} 个域名"
                f"（{len(ok_files)}/{len(files)} 个文件，{fmt_bytes(sum(f.get('bytes', 0) for f in ok_files))}）")
            results[src["idx"]] = (src, domains, files)

    # 合并去重
    with open(ALL_DOM, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(sorted(union)) + "\n")

    # 生成报告
    lines = ["# 拦截列表抓取报告", "",
             f"- 抓取时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
             f"- 来源数量：{len(sources)}",
             f"- 成功来源：{sum(1 for v in results.values() if v[1])}",
             f"- **合并去重后域名总数：{len(union):,}**", "",
             "提取口径：hosts 条目 / 纯域名行 / `||domain^` 网络拦截规则（含带 `$` 选项者）；"
             "跳过 `@@` 例外规则、元素隐藏规则和带路径的规则。“NextDNS 标称”为目录页显示的条目数，仅作参考。",
             "",
             "| # | 列表 | 状态 | NextDNS 标称 | 实际提取域名 |",
             "|---|------|------|--------------|--------------|"]
    failed = []
    for idx in sorted(results):
        src, domains, files = results[idx]
        mark = "✅" if domains else "❌"
        lines.append(f"| {idx} | {src['title']} | {mark} | {src['expected']:,} | {len(domains):,} |")
        if not domains:
            failed.append((src, files))
    lines += ["", "## 失败来源明细", ""]
    if failed:
        for src, files in failed:
            lines.append(f"### {src['title']}")
            for f in files:
                err = f.get("error", "未知")
                lines.append(f"- `{f['urls'][0]}` → {err}")
            lines.append("")
    else:
        lines.append("（无）", "")
    lines += ["## 文件明细", ""]
    for idx in sorted(results):
        src, domains, files = results[idx]
        lines.append(f"### {idx}. {src['title']}（提取 {len(domains):,}）")
        for f in files:
            if f.get("ok"):
                lines.append(f"- ✅ {fmt_bytes(f['bytes'])} / {f['lines']:,} 行 ← {f['url']}")
            else:
                lines.append(f"- ❌ {f.get('error')} ← {f['urls'][0]}")
        lines.append("")
    with open(REPORT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    out("")
    out(f"完成，用时 {time.time() - t0:.0f}s。")
    out(f"合并去重域名总数: {len(union):,}")
    out(f"输出目录: {DOM_DIR}")
    out(f"合并文件: {ALL_DOM}")
    out(f"报告: {REPORT}")
    if failed:
        out(f"失败来源: {', '.join(s['title'] for s, _ in failed)}")


if __name__ == "__main__":
    main()
