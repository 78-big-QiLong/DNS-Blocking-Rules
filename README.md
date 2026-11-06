# DNS 拦截规则合集

基于 NextDNS 官方 Blocklist Catalog 中的 **51 个**广告/跟踪器拦截列表抓取整理，提取所有 DNS 层面可拦截的域名。

- 抓取时间：2026-11-07
- 结果：**48/51 成功，合并去重后 1,519,181 个域名**
- 提取口径：hosts 条目 / 纯域名行 / `||domain^` 网络拦截规则（含 `$` 选项者）；跳过 `@@` 例外规则、元素隐藏规则和带路径的规则
- 未获取的 3 个列表：NextDNS 原生 Ads & Trackers / YouTube / Reddit 拦截——官方数据仓库 `nextdns/native-tracking-domains` 已被删除，无公开镜像

## 目录结构

```
ALL-domains-unique.txt      全部列表合并去重后的域名（151.9 万行，纯域名格式）
ALL-domains-unique.txt.gz   同上，gzip -9（10.3 MB）
ALL-domains-unique.txt.xz   同上，xz -9e（7.9 MB）
ALL-domains-unique.txt.br   同上，brotli -q 11（8.1 MB）
domains/                    每个列表单独提取的域名文件（48 个）
raw/                        原始下载文件（79 个）
scripts/fetch_blocklists.py 抓取脚本（Python 3 标准库，python -I scripts/fetch_blocklists.py 重跑即可更新）
REPORT.md                   完整抓取报告（每个文件的来源 URL、大小、行数、成败明细）
```

## 使用

- **Pi-hole / AdGuard Home / NextDNS 自定义列表**：`domains/*.txt` 或合并文件均为纯域名格式，可直接导入或订阅
- 压缩版适合存档/分发，`gunzip` / `xz -d` / `brotli -d` 解压

## 各列表提取统计

| # | 列表 | 实际提取 | # | 列表 | 实际提取 |
|---|------|---------|---|------|---------|
| 3 | AdGuard DNS filter | 189,314 | 26 | hufilter | 156 |
| 4 | OISD (big+small) | 233,424 | 27 | bkrucarci turk-adlist | 1,213 |
| 5 | AdGuard Mobile Ads | 1,058 | 28 | Frellwit's Swedish | 1,152 |
| 7 | AdGuard Tracking Protection | 10,315 | 29 | ad-wars | 1,645 |
| 8 | Goodbye Ads (AdBlock+Ultra+YouTube) | 757,793 | 30 | Liste AR | 109 |
| 9 | EasyList | 47,059 | 31 | EasyList Hebrew | 177 |
| 10 | HaGeZi Multi PRO++ | 227,608 | 32 | CertyficateIT (波兰) | 329 |
| 11 | AdGuard Base | 2,078 | 33 | Finnish Easylist | 27 |
| 12 | HaGeZi Multi PRO | 219,288 | 34 | EasyList Dutch | 60 |
| 13 | Steven Black | 77,757 | 35 | YousList | 136 |
| 14 | EasyPrivacy | 47,523 | 36 | EasyList Italy | 113 |
| 15 | HaGeZi Multi NORMAL | 171,403 | 37 | ABPindo | 419 |
| 16 | Fanboy's Annoyance | 995 | 38 | 1Hosts (Lite) | 202,951 |
| 17 | HaGeZi Multi ULTIMATE | 261,512 | 39 | Disconnect (Malvertising) | 2,735 |
| 18 | AdAway | 6,540 | 40 | RU AdList | 9,616 |
| 19 | Disconnect (Ads) | 2,700 | 41 | EasyList China | 6,024 |
| 20 | AdGuard Social Media | 48 | 42 | Anudeep's Blacklist | 42,358 |
| 21 | AdGuard Russian | 2,149 | 43 | Perflyst Smart-TV | 498 |
| 22 | Dan Pollock | 12,971 | 44 | Peter Lowe | 3,558 |
| 23 | hBlock | 478,170 | 45 | anti-AD (中文) | 110,042 |
| 24 | ShadowWhisperer Tracking | 121,085 | 46 | Disconnect (Tracking) | 34 |
| 25 | EasyList Lithuania | 65 | 47 | NoTrack | 15,214 |

（编号与 NextDNS 目录顺序一致，1/2/6 为已下架的 NextDNS 原生列表；另有 Latvian List 43、WaLLy3K 351、EasyList Czech and Slovak 98 等，完整表格见 [REPORT.md](REPORT.md)）
