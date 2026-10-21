# Independent fact-check (Oct 21 2026)

**What was run.** After all 21 pages were written, five separate fact-check sub-agents (fc1 to fc5) checked the
factual claims and cited sources on every page. None of them wrote any page it checked (the pages were written
by eight other writer agents). Each followed docs/fact-check/BRIEF.md: list every non-obvious claim (numbers,
dates, rules, phone numbers, fees, providers, programs, statutes, populations, prices, lifespans), verify it,
then correct, soften or remove it in place, re-run build.py, check.py, similarity.py and grep_check.py on its
pages, and log every claim. Claim-by-claim tables: docs/fact-check/fc1.md to fc5.md.

**Method limit (read this).** This environment's network policy blocks direct page fetches (WebFetch and curl
fail for yumaaz.gov, yumacountyaz.gov, roc.az.gov, weather.gov and nearly every other source). Claims were
verified against WebSearch result summaries of the named official or credible page, usually restricted to that
source's domain, not by opening the page. Each checker had a budget of about 20 searches; fc3 kept two hedged
general pump-symptom claims without a fresh search (marked in fc3.md). To re-verify by opening every source,
allow those domains in the environment's network settings and re-run the checkers.

| Checker | Pages | Claims checked | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc1 | /, /how-it-works/, /contact/, /about/, /services/ | 40 | 32 | 5 | 2 | 1 |
| fc2 | /service-areas/, /faq/, /pool-service, /pool-cleaning | 79 | 62 | 10 | 5 | 2 |
| fc3 | /pool-repair/, /pool-equipment-repair/, /pool-pump-repair/ | 67 | 46 | 9 | 6 | 4 |
| fc4 | /pool-tile-cleaning/, /green-pool-cleanup/, /my-pool-is-green/ | 65 | 54 | 3 | 5 | 3 |
| fc5 | /pool-maintenance-cost/, /is-a-pool-service-worth-it/, /yuma-pool-maintenance-schedule/, privacy, terms | 75 | 66 | 1 | 5 | 3 |
| **Total** | 21 pages (404 has no factual claims) | **326** | **260** | **28** | **23** | **13** |

(fc3's 67 include 2 claims kept without a fresh search.)

**Most important fixes.**
- **"About 71,000 winter visitors"** (a 2017 to 2018 Arizona State University study for Visit Yuma) was in the
  research file but could not be found again by four checkers or the lead. Removed from every page; pages now
  use Yuma County's confirmed statement that the county's population grows by about 90,000 in winter.
- **Dust storm timing:** the NOAA memo's "late July and early August" peak is stated for another area. Pages now
  say only what the memo supports for Yuma: the low desert has the most dust reports, and reports rise sharply
  in July.
- **Yuma County drain rule:** chlorine must be below 1 ppm only for water released somewhere other than the
  sanitary sewer (pages had applied it to all drainage).
- **Prices:** a salt cell figure of "up to about $1,100" and a gas heater install range of "$1,500 to $6,000" came
  from Angi city pages, not its national tables; replaced with Angi's national figures. A HomeGuide heat pump
  lifespan could not be found and was removed. Filter and cartridge figures were narrowed to what Angi shows.
  Every price left is a named publisher's national range with "real quotes vary"; no Yuma price is published
  and none is implied.
- **Visit frequency:** Angi ties every-other-week service to moderate use and monthly to light use; corrected.
- **Yuma County green pools:** "one of the major breeding sources" of West Nile mosquitoes, as the county says.
- **ROC complaints:** the ROC does take homeowner complaints, generally within two years of the work; added.
- Electric providers: the APS map labels Yuma, Somerton, San Luis and Wellton but does not settle boundaries;
  pages say the name on the electric bill decides. Wellton's power is the Wellton-Mohawk Irrigation and Drainage
  District (confirmed on the district's and town's pages).
- No page says or implies the line does pool work, checks licenses, or that any company is licensed, insured or
  rated; no company is named; no page gives chemical doses or acid steps; no place outside Yuma County appears.
