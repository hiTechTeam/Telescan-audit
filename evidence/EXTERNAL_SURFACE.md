# Authorized External Smoke Observations

**Observed (UTC):** 2026-09-01T09:38:44Z  
**Method:** read-only HTTPS `GET`, redirects followed, 15-second timeout, no
credentials or user data  
**TLS verification:** successful for every request (`curl` result `0`)

| Endpoint | HTTP result | Elapsed |
| --- | --- | --- |
| `https://api.tgtelescan.ru/health/live` | 200 | 0.222109 s |
| `https://api.tgtelescan.ru/health/ready` | 200 | 0.225120 s |
| `https://tgtelescan.ru/privacy` | 200 | 0.394299 s |
| `https://tgtelescan.ru/terms` | 200 | 0.304405 s |

These observations confirm public reachability and TLS/HTTP success immediately
after the September 1 deployment. They are not a port scan, penetration test,
content-integrity proof, or substitute for the scoped external-surface review.
