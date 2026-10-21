# Fact-check fc1 (Oct 21 2026)

Checker: fc1 (independent; wrote none of these pages). Pages: `/` (index.html), `/how-it-works/`, `/contact/`, `/about/`, `/services/`.
Method: WebSearch, standard mode, restricted to the official or named source domain; search-result summaries of the cited page used as evidence, plus docs/research/*.md where already verified. Searches used: 19 (budget about 20).

Validation after fixes: `build.py --out /tmp/claude-0/fc1/dist` OK; `check.py --only` 0 errors, 0 warnings on all five pages; `similarity.py` no FAIL (highest pair 2.0% Yuma mixed, 1.2% vs Tucson, 1.2% vs Phoenix, no shared 8-word runs); `grep_check.py` 0 hits.

Rule sweep (all five pages): nothing implies the line does pool work; no claim of a Spanish-speaking phone assistant (how-it-works says the ES button changes the website only, not the call); no company named; every place is in Yuma County (Yuma, Fortuna Foothills, Somerton, San Luis, Wellton, Gadsden, Colorado River, Interstate 8, U.S. 95, Wellton-Mohawk Valley, Yuma Valley); no em/en dashes; the CDC drowning "number one" wording is not used on these pages; no DIY dosing.

## / (home)

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| About 118 days a year at 100 F or more (1991 to 2020) | weather.gov/psr/ExtremeTemps (search) | confirmed | Yuma middle column: 118 (1991 to 2020) |
| Usually late April into early October | weather.gov/psr/ExtremeTemps, FirstandLastTemperatures | confirmed | Normal first Apr 25, last Oct 6 |
| About 25 days at 110 F or more | weather.gov/psr/ExtremeTemps | confirmed | |
| Normal July high 106.7 F | weather.gov/media/psr/Climate/July2026Climate.pdf (search) | confirmed | 108.4 observed vs 106.7 normal (1991 to 2020) |
| Visit Yuma: sun about 91% of daylight hours | visityuma.com/about-yuma/climate (search) | confirmed | 4,055 of 4,456 hours; attributed to Visit Yuma |
| Sunlight breaks down chlorine; cyanuric acid stabilizer | CDC home pool page; research licensing-safety #17 | confirmed | |
| CDC: free chlorine 2 ppm or more with stabilizer, pH 7.0 to 7.8 | cdc.gov home pool page (search) | confirmed | |
| City of Yuma treats Colorado River water | yumaaz.gov water quality report / FAQ (search) | confirmed | |
| City FAQ calls water hard, 18 to 22 grains per gallon | yumaaz.gov Water FAQs (search) | confirmed | |
| Monsoon season June 15 to September 30 (NWS) | weather.gov/media/twc/Monsoon.pdf (search) | confirmed | |
| NOAA study names Yuma; dust storms most common late July and early August | TM-290 (search) | softened | Late July/early August peak is stated for Phoenix; memo groups Yuma into the low-desert region with the most dust reports, July rise, outflow reaching the Colorado River. Reworded to that. |
| 2017 to 2018 Visit Yuma study: about 71,000 winter visitors, 30+ days, December to May | visityuma.com study page, tourism.az.gov PDF, open search (3 searches) | removed | 30-day definition confirmed but the 71,000 figure did not appear in any summary; sentence and source removed |
| Yuma County: population grows by about 90,000 in winter | yumacountyaz.gov About the County (search) | confirmed | Another county page says 76,000+; kept as the county's own figure |
| Yuma County Public Health: green pools a major breeding source of West Nile mosquitoes | yumacountyaz.gov News 2148 (search) | corrected | County says "one of the major breeding sources"; wording fixed |
| HomeGuide: weekly or every-other-week service about $80 to $150 a month | homeguide.com pool-maintenance-cost (search) | confirmed | Says quotes vary; not presented as the line's price |
| Liability insurance is not a condition of an ROC license | roc.az.gov/before-hire, FAQ (search) | confirmed | Only workers' comp (with employees) |
| ROC contractor search lookup | roc.az.gov/contractor-search | confirmed | |
| Town descriptions (Wellton in Wellton-Mohawk Valley, Somerton in Yuma Valley, Gadsden on U.S. 95, San Luis at the border, county seat) | docs/research/towns.md | confirmed | From verified fact bank |

Totals: 18 checked, 15 confirmed, 1 corrected, 1 softened, 1 removed.

## /how-it-works/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| R-6 is the ROC class for home pool service and repair | roc.az.gov/license-classifications (search) | confirmed | |
| Liability insurance not a condition of an ROC license; not listed in the search | roc.az.gov/before-hire, FAQ (search) | confirmed | |
| Contractor search shows whether the license is active and its classification | ROC Consumer Guide PDF (search) | confirmed | |
| Sources list (classifications, before-hire, FAQ, contractor search) | domain and topic match | confirmed | |

Totals: 4 checked, 4 confirmed.

## /contact/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Homeowner can file a complaint with the ROC about a licensee | roc.az.gov/file-complaint, complaint-process-legal (search) | softened | Added "generally within two years of the date the work was last done" (remodel/repair window); added File a Formal Complaint as a source |
| Contractor search lists status and recent complaints | ROC Consumer Guide PDF (search) | corrected | It shows closed complaints from the prior two years; wording fixed, guide added as a source |
| Gas smell: leave, no switches/flames, call 911 and Southwest Gas 877-860-6020 | swgas.com/en/safety (search) | confirmed | |
| Never combine pool chemicals; keep in original container away from children | CDC Pool Chemical Safety (research #19, #20) | confirmed | |
| Calls may be recorded | src/pages/privacy-policy.html | confirmed | Consistent with the site's privacy policy |

Totals: 5 checked, 3 confirmed, 1 corrected, 1 softened.

## /about/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| d/b/a of Dominion Digital Group | INTAKE.md | confirmed | |
| "a recorded assistant answers" | INTAKE.md | corrected | It is an automated assistant; "recorded" was misleading |
| Contractor search shows status, class, recent closed complaints, bond | ROC Consumer Guide PDF (search) | confirmed | |
| Workers' comp (with employees) is the only insurance the ROC requires; insurance not in search | roc.az.gov/before-hire (search) | confirmed | |
| City of Yuma describes its Colorado River water as hard | yumaaz.gov Water FAQs (search) | confirmed | |
| No published source lists Yuma-specific pool service prices | docs/research/costs-equipment.md | confirmed | |

Totals: 6 checked, 5 confirmed, 1 corrected.

## /services/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| "A recorded assistant picks up" | INTAKE.md | corrected | Changed to automated assistant |
| CDC: pH 7.0 to 7.8, free chlorine at least 1 ppm, 2 ppm with cyanuric acid | cdc.gov home pool page (search) | confirmed | |
| NWS: about 118 days a year at 100 F or more | weather.gov/psr/ExtremeTemps (search) | confirmed | |
| R-6 covers service and minor repair; excludes gas lines, electrical past the first disconnect, potable water connections | roc.az.gov/license-classifications (search) | confirmed | |
| Southwest Gas 877-860-6020, leave and call 911 | swgas.com/en/safety (search) | confirmed | |
| Yuma County Public Health: green pools a major breeding source | yumacountyaz.gov News 2148 (search) | corrected | "one of the major breeding sources" |
| City of Yuma water hard, 18 to 22 grains per gallon | yumaaz.gov Water FAQs (search) | confirmed | |

Totals: 7 checked, 5 confirmed, 2 corrected.

## Grand totals

40 claims checked: 32 confirmed, 5 corrected, 2 softened, 1 removed. Searches used: 19.
