# Authorized External Smoke Observations

**Observed (UTC):** 2026-09-02T20:31:00Z

**Method:** read-only HTTPS `GET`, redirects followed, 15-second timeout, no
credentials or user data

| Endpoint | HTTP result | Observation |
| --- | --- | --- |
| `https://api.tgtelescan.ru/health/live` | 200 | API process live |
| `https://api.tgtelescan.ru/health/ready` | 200 | API and database ready |
| `https://tgtelescan.ru/privacy` | 200 | Approved legal version/hash |
| `https://tgtelescan.ru/terms` | 200 | Approved legal version/hash |
| `https://api.tgtelescan.ru/privacy` | 200 | Same approved legal version/hash |
| `https://api.tgtelescan.ru/terms` | 200 | Same approved legal version/hash |
| `https://api.tgtelescan.ru/docs` | 404 | Public Swagger denied |
| `https://api.tgtelescan.ru/openapi.json` | 404 | Public OpenAPI denied |

`api.tgtelescan.ru` resolved to the Netherlands relay `212.69.87.142` and
`tgtelescan.ru` resolved to the Moscow origin `89.169.153.38`, matching the
documented topology. Both TLS certificates validated successfully. The API
certificate was valid through November 15, 2026; the main-domain certificate
was valid through November 10, 2026.

The four legal pages served approved version `2026-09-01` and source SHA-256
`f3bddc01a0013a89086044509ba85e1e63edc6bde7e45732a7e0c9803257045e`.

These observations are not a port scan, penetration test, or substitute for
the scoped production-attestation collector.
