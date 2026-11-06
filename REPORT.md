# 拦截列表抓取报告

- 抓取时间：2026-11-07 01:48:02
- 来源数量：51
- 成功来源：48
- **合并去重后域名总数：1,519,181**

提取口径：hosts 条目 / 纯域名行 / `||domain^` 网络拦截规则（含带 `$` 选项者）；跳过 `@@` 例外规则、元素隐藏规则和带路径的规则。“NextDNS 标称”为目录页显示的条目数，仅作参考。

| # | 列表 | 状态 | NextDNS 标称 | 实际提取域名 |
|---|------|------|--------------|--------------|
| 1 | NextDNS 广告和跟踪器拦截列表 | ❌ | 79,006 | 0 |
| 2 | NextDNS YouTube 广告拦截 | ❌ | 2 | 0 |
| 3 | AdGuard DNS filter | ✅ | 189,177 | 189,314 |
| 4 | OISD | ✅ | 232,695 | 233,424 |
| 5 | AdGuard Mobile Ads filter | ✅ | 952 | 1,058 |
| 6 | NextDNS Reddit 广告拦截 | ❌ | 3 | 0 |
| 7 | AdGuard Tracking Protection filter | ✅ | 119,138 | 10,315 |
| 8 | Goodbye Ads | ✅ | 277,778 | 757,793 |
| 9 | EasyList | ✅ | 46,893 | 47,059 |
| 10 | HaGeZi - Multi PRO++ | ✅ | 238,296 | 227,608 |
| 11 | AdGuard Base filter | ✅ | 59,460 | 2,078 |
| 12 | HaGeZi - Multi PRO | ✅ | 222,630 | 219,288 |
| 13 | Steven Black | ✅ | 77,769 | 77,757 |
| 14 | EasyPrivacy | ✅ | 47,126 | 47,523 |
| 15 | HaGeZi - Multi NORMAL | ✅ | 178,087 | 171,403 |
| 16 | Fanboy's Annoyance List | ✅ | 920 | 995 |
| 17 | HaGeZi - Multi ULTIMATE | ✅ | 273,572 | 261,512 |
| 18 | AdAway | ✅ | 6,541 | 6,540 |
| 19 | Disconnect (Ads) | ✅ | 2,700 | 2,700 |
| 20 | AdGuard Social Media filter | ✅ | 48 | 48 |
| 21 | AdGuard Russian filter | ✅ | 1,965 | 2,149 |
| 22 | someonewhocares.org (Dan Pollock) | ✅ | 12,983 | 12,971 |
| 23 | hBlock | ✅ | 478,220 | 478,170 |
| 24 | ShadowWhisperer Tracking | ✅ | 121,085 | 121,085 |
| 25 | EasyList Lithuania | ✅ | 32 | 65 |
| 26 | hufilter | ✅ | 92 | 156 |
| 27 | Latvian List | ✅ | 40 | 43 |
| 28 | EasyList Czech and Slovak | ✅ | 93 | 98 |
| 29 | bkrucarci turk-adlist | ✅ | 1,214 | 1,213 |
| 30 | Frellwit's Swedish Hosts File | ✅ | 1,152 | 1,152 |
| 31 | ad-wars | ✅ | 1,646 | 1,645 |
| 32 | Liste AR | ✅ | 73 | 109 |
| 33 | EasyList Hebrew | ✅ | 140 | 177 |
| 34 | CertyficateIT (波兰) | ✅ | 1,142 | 329 |
| 35 | Finnish Easylist Addition | ✅ | 15 | 27 |
| 36 | Personal Blocklist by WaLLy3K | ✅ | 351 | 351 |
| 37 | EasyList Dutch | ✅ | 56 | 60 |
| 38 | YousList (韩语) | ✅ | 626 | 136 |
| 39 | EasyList Italy | ✅ | 93 | 113 |
| 40 | ABPindo (印尼/马来) | ✅ | 125 | 419 |
| 41 | 1Hosts (Lite) | ✅ | 102,259 | 202,951 |
| 42 | Disconnect (Malvertising) | ✅ | 2,736 | 2,735 |
| 43 | RU AdList | ✅ | 9,088 | 9,616 |
| 44 | HaGeZi - Multi LIGHT | ✅ | 87,809 | 92,161 |
| 45 | EasyList China | ✅ | 5,903 | 6,024 |
| 46 | Anudeep's Blacklist | ✅ | 42,358 | 42,358 |
| 47 | Perflyst's Smart-TV Blocklist | ✅ | 498 | 498 |
| 48 | Peter Lowe | ✅ | 3,559 | 3,558 |
| 49 | anti-AD (中文) | ✅ | 110,042 | 110,042 |
| 50 | Disconnect (Tracking) | ✅ | 34 | 34 |
| 51 | NoTrack Tracker Blocklist | ✅ | 15,214 | 15,214 |

## 失败来源明细

### NextDNS 广告和跟踪器拦截列表
- `https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/ads--trackers` → RuntimeError: https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/ads--trackers -> HTTP 404 | https://raw.githubusercontent.com/nextdns/native-tracking-domains/main/domains/ads--trackers -> HTTP 404

### NextDNS YouTube 广告拦截
- `https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/youtube-ads` → RuntimeError: https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/youtube-ads -> HTTP 404 | https://raw.githubusercontent.com/nextdns/native-tracking-domains/main/domains/youtube-ads -> HTTP 404

### NextDNS Reddit 广告拦截
- `https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/reddit-ads` → RuntimeError: https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/reddit-ads -> HTTP 404 | https://raw.githubusercontent.com/nextdns/native-tracking-domains/main/domains/reddit-ads -> HTTP 404

## 文件明细

### 1. NextDNS 广告和跟踪器拦截列表（提取 0）
- ❌ RuntimeError: https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/ads--trackers -> HTTP 404 | https://raw.githubusercontent.com/nextdns/native-tracking-domains/main/domains/ads--trackers -> HTTP 404 ← https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/ads--trackers

### 2. NextDNS YouTube 广告拦截（提取 0）
- ❌ RuntimeError: https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/youtube-ads -> HTTP 404 | https://raw.githubusercontent.com/nextdns/native-tracking-domains/main/domains/youtube-ads -> HTTP 404 ← https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/youtube-ads

### 3. AdGuard DNS filter（提取 189,314）
- ✅ 4.4MB / 191,811 行 ← https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt

### 4. OISD（提取 233,424）
- ✅ 4.8MB / 232,748 行 ← https://big.oisd.nl/domainswild
- ✅ 1.3MB / 60,767 行 ← https://small.oisd.nl/domainswild

### 5. AdGuard Mobile Ads filter（提取 1,058）
- ✅ 23.5KB / 1,072 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/adservers.txt
- ✅ 90.2KB / 725 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/specific_app.txt
- ✅ 405.1KB / 6,557 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/specific_web.txt

### 6. NextDNS Reddit 广告拦截（提取 0）
- ❌ RuntimeError: https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/reddit-ads -> HTTP 404 | https://raw.githubusercontent.com/nextdns/native-tracking-domains/main/domains/reddit-ads -> HTTP 404 ← https://raw.githubusercontent.com/nextdns/native-tracking-domains/master/domains/reddit-ads

### 7. AdGuard Tracking Protection filter（提取 10,315）
- ✅ 123.9KB / 4,618 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers.txt
- ✅ 116.8KB / 4,951 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt
- ✅ 37.1KB / 1,390 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/mobile.txt
- ✅ 256.9KB / 6,343 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/specific.txt
- ✅ 18.1KB / 780 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_url.txt

### 8. Goodbye Ads（提取 757,793）
- ✅ 7.3MB / 277,855 行 ← https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Formats/GoodbyeAds-AdBlock-Filter.txt
- ✅ 11.0MB / 459,216 行 ← https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Formats/GoodbyeAds-Ultra-AdBlock-Filter.txt
- ✅ 3.4MB / 97,669 行 ← https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Formats/GoodbyeAds-YouTube-AdBlock-Filter.txt

### 9. EasyList（提取 47,059）
- ✅ 2.0MB / 78,425 行 ← https://easylist.to/easylist/easylist.txt

### 10. HaGeZi - Multi PRO++（提取 227,608）
- ✅ 4.6MB / 227,654 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/pro.plus.txt
- ✅ 4.2MB / 227,654 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/pro.plus-onlydomains.txt

### 11. AdGuard Base filter（提取 2,078）
- ✅ 37.3KB / 1,499 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers.txt
- ✅ 9.5KB / 340 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers_firstparty.txt
- ✅ 2.0MB / 25,038 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/specific.txt
- ✅ 24.3KB / 592 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/general_url.txt
- ✅ 4.0KB / 137 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/cryptominers.txt
- ✅ 863.8KB / 14,789 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/foreign.txt

### 12. HaGeZi - Multi PRO（提取 219,288）
- ✅ 4.5MB / 219,334 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/pro.txt
- ✅ 4.1MB / 219,334 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/pro-onlydomains.txt

### 13. Steven Black（提取 77,757）
- ✅ 2.2MB / 84,577 行 ← https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts

### 14. EasyPrivacy（提取 47,523）
- ✅ 1.4MB / 57,267 行 ← https://easylist.to/easylist/easyprivacy.txt

### 15. HaGeZi - Multi NORMAL（提取 171,403）
- ✅ 3.5MB / 171,431 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/multi.txt
- ✅ 3.2MB / 171,431 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/multi-onlydomains.txt

### 16. Fanboy's Annoyance List（提取 995）
- ✅ 1.7MB / 50,855 行 ← https://easylist.to/easylist/fanboy-annoyance.txt

### 17. HaGeZi - Multi ULTIMATE（提取 261,512）
- ✅ 5.3MB / 261,563 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/ultimate.txt
- ✅ 4.8MB / 261,563 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/ultimate-onlydomains.txt

### 18. AdAway（提取 6,540）
- ✅ 237.7KB / 10,608 行 ← https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt

### 19. Disconnect (Ads)（提取 2,700）
- ✅ 42.6KB / 2,705 行 ← https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt

### 20. AdGuard Social Media filter（提取 48）
- ✅ 5.7KB / 147 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/social_trackers.txt
- ✅ 25.2KB / 534 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/popups.txt

### 21. AdGuard Russian filter（提取 2,149）
- ✅ 57.4KB / 2,246 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/adservers.txt
- ✅ 643B / 15 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/adservers_firstparty.txt
- ✅ 18.0KB / 844 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/general_url.txt
- ✅ 44.3KB / 429 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/specific.txt
- ✅ 3.3KB / 140 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/adservers_firstparty.txt
- ✅ 556.3KB / 11,613 行 ← https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/specific.txt

### 22. someonewhocares.org (Dan Pollock)（提取 12,971）
- ✅ 355.7KB / 13,298 行 ← https://someonewhocares.org/hosts/zero/hosts

### 23. hBlock（提取 478,170）
- ✅ 13.3MB / 478,239 行 ← https://hblock.molinero.dev/hosts

### 24. ShadowWhisperer Tracking（提取 121,085）
- ✅ 2.5MB / 121,096 行 ← https://raw.githubusercontent.com/ShadowWhisperer/BlockLists/master/Lists/Tracking

### 25. EasyList Lithuania（提取 65）
- ✅ 53.0KB / 1,237 行 ← https://raw.githubusercontent.com/EasyList-Lithuania/easylist_lithuania/master/easylistlithuania.txt
- ✅ 1.9KB / 62 行 ← https://raw.githubusercontent.com/EasyList-Lithuania/easylist_lithuania/master/EasyListLithuaniaHosts.txt

### 26. hufilter（提取 156）
- ✅ 52.8KB / 1,462 行 ← https://raw.githubusercontent.com/hufilter/hufilter/master/sections/ads.txt
- ✅ 3.9KB / 104 行 ← https://raw.githubusercontent.com/hufilter/hufilter/master/sections/trackers.txt
- ✅ 679B / 18 行 ← https://raw.githubusercontent.com/hufilter/hufilter/master/sections/security.txt
- ✅ 4.0KB / 100 行 ← https://raw.githubusercontent.com/hufilter/hufilter/master/sections/selfpromo.txt
- ✅ 9.2KB / 239 行 ← https://raw.githubusercontent.com/hufilter/hufilter/master/sections/annoyances.txt
- ✅ 2.1KB / 43 行 ← https://raw.githubusercontent.com/hufilter/hufilter/master/sections/antiadblock.txt

### 27. Latvian List（提取 43）
- ✅ 15.8KB / 467 行 ← https://raw.githubusercontent.com/Latvian-List/adblock-latvian/master/lists/latvian-list.txt

### 28. EasyList Czech and Slovak（提取 98）
- ✅ 21.3KB / 677 行 ← https://raw.githubusercontent.com/tomasko126/easylistczechandslovak/master/filters.txt

### 29. bkrucarci turk-adlist（提取 1,213）
- ✅ 33.1KB / 1,236 行 ← https://raw.githubusercontent.com/bkrucarci/turk-adlist/master/hosts

### 30. Frellwit's Swedish Hosts File（提取 1,152）
- ✅ 34.9KB / 1,160 行 ← https://raw.githubusercontent.com/lassekongo83/Frellwits-filter-lists/master/Frellwits-Swedish-Hosts-File.txt

### 31. ad-wars（提取 1,645）
- ✅ 48.2KB / 1,739 行 ← https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts

### 32. Liste AR（提取 109）
- ✅ 60.4KB / 1,666 行 ← https://easylist-downloads.adblockplus.org/liste_ar.txt

### 33. EasyList Hebrew（提取 177）
- ✅ 229.6KB / 1,579 行 ← https://raw.githubusercontent.com/easylist/EasyListHebrew/master/EasyListHebrew.txt

### 34. CertyficateIT (波兰)（提取 329）
- ✅ 336.4KB / 6,125 行 ← https://raw.githubusercontent.com/MajkiIT/polish-ads-filter/master/polish-adblock-filters/adblock.txt

### 35. Finnish Easylist Addition（提取 27）
- ✅ 72.2KB / 1,279 行 ← https://raw.githubusercontent.com/finnish-easylist-addition/finnish-easylist-addition/master/Finland_adb.txt
- ✅ 4.8KB / 75 行 ← https://raw.githubusercontent.com/finnish-easylist-addition/finnish-easylist-addition/master/Finland_adb_uBO_extras.txt

### 36. Personal Blocklist by WaLLy3K（提取 351）
- ✅ 8.2KB / 423 行 ← https://v.firebog.net/hosts/static/w3kbl.txt

### 37. EasyList Dutch（提取 60）
- ✅ 67.5KB / 1,578 行 ← https://easylist-downloads.adblockplus.org/easylistdutch.txt

### 38. YousList (韩语)（提取 136）
- ✅ 352.5KB / 7,837 行 ← https://raw.githubusercontent.com/yous/YousList/master/youslist.txt

### 39. EasyList Italy（提取 113）
- ✅ 186.0KB / 4,261 行 ← https://easylist-downloads.adblockplus.org/easylistitaly.txt

### 40. ABPindo (印尼/马来)（提取 419）
- ✅ 307.3KB / 10,309 行 ← https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/subscriptions/abpindo.txt
- ✅ 4.5KB / 143 行 ← https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/subscriptions/abpindo_hosts.txt
- ✅ 2.5KB / 142 行 ← https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/subscriptions/domain.txt

### 41. 1Hosts (Lite)（提取 202,951）
- ✅ 4.7MB / 202,971 行 ← https://raw.githubusercontent.com/badmojr/1Hosts/master/Lite/domains.txt

### 42. Disconnect (Malvertising)（提取 2,735）
- ✅ 43.1KB / 2,739 行 ← https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt

### 43. RU AdList（提取 9,616）
- ✅ 1.1MB / 27,703 行 ← https://easylist-downloads.adblockplus.org/ruadlist.txt

### 44. HaGeZi - Multi LIGHT（提取 92,161）
- ✅ 2.0MB / 92,175 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/light.txt
- ✅ 1.8MB / 92,175 行 ← https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/light-onlydomains.txt

### 45. EasyList China（提取 6,024）
- ✅ 485.8KB / 17,870 行 ← https://easylist-downloads.adblockplus.org/easylistchina.txt

### 46. Anudeep's Blacklist（提取 42,358）
- ✅ 1.3MB / 42,542 行 ← https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt

### 47. Perflyst's Smart-TV Blocklist（提取 498）
- ✅ 16.2KB / 631 行 ← https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt

### 48. Peter Lowe（提取 3,558）
- ✅ 93.0KB / 3,574 行 ← https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext

### 49. anti-AD (中文)（提取 110,042）
- ✅ 2.0MB / 110,047 行 ← https://anti-ad.net/domains.txt

### 50. Disconnect (Tracking)（提取 34）
- ✅ 613B / 39 行 ← https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt

### 51. NoTrack Tracker Blocklist（提取 15,214）
- ✅ 602.9KB / 15,226 行 ← https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/notrack-blocklist.txt
- ❌ RuntimeError: https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/notrack-tracker.txt -> HTTP 404 | https://gitlab.com/quidsup/notrack-blocklists/-/raw/main/notrack-tracker.txt -> HTTP 404 ← https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/notrack-tracker.txt

