# Fact-check fc3: pool-repair, pool-equipment-repair, pool-pump-repair (Oct 21 2026)

Checker fc3 did not write these pages. Method: WebSearch (standard mode, restricted to the publisher or official domain), plus docs/research/*.md for facts already verified there (each one checked against the page's wording). Searches used: 23 (cap about 22). After the coordinator's note, the NOAA dust "peak late July and early August" line (stated for Phoenix in TM-290, not Yuma) was rewritten on both pages that carried it. No page here used the 71,000 winter visitor figure.

Validation (build in /tmp/claude-0/fc3/dist): check.py 0 errors on all three URLs; grep_check.py 0 hits; similarity.py no FAIL (max Jaccard against Tucson 0.9%, against Phoenix 0.5%, no shared 8-word runs; one new sentence first collided with Tucson and was reworded).

## /pool-repair/ (src/pages/pool-repair.html)

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Bucket test steps (pump off, bucket on step, mark, 24 hours) | EPA WaterSense pool guide (search) | confirmed | |
| Leak likely if loss > 2 in/week, > 3 in hot dry areas | EPA WaterSense pool guide (search) | confirmed | |
| Evaporation 12,000 to 31,000 gal/yr; cover cuts up to 95% | research/water-utilities-rules, climate | confirmed | |
| About 118 days at or above 100 F | NWS normals (research) | confirmed | |
| "Angi notes a bigger drop with the pump on points to pipes" | not found | removed | replaced with EPA's confirmed advice to repeat a manual leak test and check the auto fill valve |
| Angi leak-location list, dye testing, "digging blind" | EPA guide lists liner, pump seal, piping, pool-to-pipe connection, edges, joints | corrected | re-attributed to EPA's list; dye-test sentence dropped |
| Pressure test is a first step, excavation a last resort | Angi leak detection guide (search) | confirmed | |
| City of Yuma: call Utilities (928) 373-4500 before draining; Director approval for sewer; private cleanout, no manhole, not into street | research/water-utilities-rules 18 to 19 | confirmed | |
| City of Yuma water 18 to 22 grains per gallon | research | confirmed | |
| Angi: low pH and low calcium hardness etch a finish | not re-checked | softened | now "Angi's resurfacing tips link poor water chemistry to finish damage" |
| Plaster about $6 to $8 per sq ft (HomeGuide) | HomeGuide resurfacing pages (search) | confirmed | wording now "resurfacing pages" |
| Bob Vila: some epoxies cure underwater; "works underwater" label caveat | Bob Vila pool patch review (search) | confirmed | |
| CPSC: underwater lighting, older pools, GFCI test monthly | CPSC (search) | confirmed | |
| VGB Act Dec 2007; public pools required, home pools recommended; never swim with broken cover | research/licensing-safety 23, 26 | confirmed | |
| CDC: drowning leading cause of death ages 1 to 4 | research 22 | confirmed | |
| Angi repair: avg $725, $243 to $1,212, in-ground $350 to $2,700, leak repair $10 to $3,500, drain $180 to $230 | Angi 2026 repair guide (search) | confirmed | |
| Angi leak detection: avg $300, $100 to $1,000, in-ground $400 to $1,000, pressure test $200 to $500, digging $500 to $5,000 | Angi 2026 leak detection guide (search) | confirmed | |
| R-6 scope and exclusions (gas, electrical past first disconnect, potable water, full plaster or pebble replacement) | roc.az.gov License Classifications (search) | confirmed | |
| "A full new finish calls for B-5" (FAQ) | ROC search showed no B-5 scope text on resurfacing | softened | now: ask which classification; ROC lists pool building classifications such as B-5 separately |
| A.R.S. 32-1121 small-job exemption about $1,000, never with a permit | azleg.gov / ROC 2024 book (search) | confirmed | "about $1,000" wording kept, as no amendment was found |
| ROC contractor search | research | confirmed | |

Sources removed: three Angi leak articles that no longer back any sentence.
Totals: 21 claims checked, 16 confirmed, 1 corrected, 2 softened, 2 removed (one replaced with a confirmed EPA fact).

## /pool-equipment-repair/ (src/pages/pool-equipment-repair.html)

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| PHTA: clean or backwash as needed, check pumps, filters, heaters monthly | research costs-equipment 10 | confirmed | |
| Angi: inspect salt cell every two months | Angi salt pool checklist (search) | confirmed | |
| Cartridge element 2 to 3 years | Angi pages give 1 to 2, 2 to 3, 2 to 4 | corrected | now "about 1 to 3 years (Angi's pages vary)" in FAQ and table |
| Sand 3 to 5 years; glass 8 to 10+; DE up to 10 | Angi (search, research 48 to 49) | confirmed | |
| Gas heater 5 to 10 years; heat pump 10+ (Angi) | Angi lifespan article (search) | confirmed | |
| Heat pump "up to 15 years" (HomeGuide) | not found on HomeGuide | removed | HomeGuide heater source removed |
| Salt cell 3 to 7 years | Angi checklist (search) | confirmed | |
| "Heat, hard water and heavy use push lifespans to the short end" | Angi: year-round pools change sand sooner | softened | now tied to Angi's year-round-use note |
| Replace heater when yearly repairs reach about half of new price | research 39 | confirmed | |
| Gas smell steps; Southwest Gas 877-860-6020, customer or not | swgas.com (search) | confirmed | |
| City of Yuma hardness 18 to 22 gpg; NWS 118 days | research | confirmed | |
| NOAA: dust storms peak late July and early August in Yuma | coordinator note (TM-290 states this for Phoenix) | corrected | now: low desert, which includes Yuma, has the most dust reports, rising sharply in July |
| Angi filter gauge: clean at 8 to 10 psi above normal, normal often 10 to 20 | Angi filter cleaning article (search) | confirmed | |
| Angi heater troubleshooting list (ignition, gas valve, flame sensor, scale) | not re-checked | softened | shortened to general causes, all inside the cabinet left to a professional |
| DOE: heat pump moves heat from air; works best in warm air | cited DOE PDFs not checked | softened | kept only the plain description; two DOE PDFs removed from sources |
| APS: turn off pool heater in summer; APS serves Yuma, Somerton, San Luis | aps.com (search), research 12 | confirmed | |
| HomeGuide: cells cleaned every 3 to 4 months | Angi checklist says at least every three months | corrected | now attributed to Angi; HomeGuide salt source removed |
| Salt cell replacement "few hundred to about $1,100" (Angi) | Angi national guide $200 to $700; $1,100 only on other-city pages | corrected | now "about $200 to $700" (Angi 2026 maintenance cost guide, source added) |
| CDC chemical storage basics | research 19 to 20 | confirmed | |
| APS TOU on-peak 4 to 7 p.m. weekdays; super off-peak Nov to Apr 10 a.m. to 3 p.m.; run pump off-peak | aps.com (search) | confirmed | |
| DOE: since 2025 many replacement motors must be variable speed | energy.gov (search) | confirmed | |
| Angi heater repair avg $476, $166 to $798 | Angi 2026 (search) | confirmed | |
| Gas heater installed $1,500 to $6,000 (Angi national) | appears on Angi city pages, not the national table | corrected | now national: average about $3,100, most $1,864 to $4,351, all types |
| Heat pump installed $2,500 to $7,500 | Angi 2026 (search) | confirmed | |
| Filter installed: cartridge $200 to $1,600, sand $300 to $1,200, DE $520 to $2,000 | Angi pages conflict (main guide: sand $500 to $1,200, cartridge $700 to $1,600, DE $1,200 to $2,500) | softened | one row: roughly $200 to $2,500 by type and size, pages differ |
| R-6 excludes gas lines and electrical past first disconnect | ROC (search) | confirmed | |

Totals: 26 claims checked, 15 confirmed, 6 corrected, 4 softened, 1 removed.

## /pool-pump-repair/ (src/pages/pool-pump-repair.html)

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Pump life about 8 to 15 years (Angi) | Angi lifespan article (search) | confirmed | |
| Replace when repair passes about 50% of a new pump (Angi) | Angi (search) | confirmed | |
| ENERGY STAR: 24 h to 6 h cuts energy 75% | energystar.gov (search) | confirmed | |
| ENERGY STAR: half speed uses about one eighth the energy | energystar.gov (search) | confirmed | |
| ENERGY STAR suggests several short run periods for debris | not found | removed | |
| APS on-peak 4 to 7 p.m. weekdays, older plans 3 to 8 p.m., run pump off-peak | aps.com (search), research 14 | confirmed | |
| APS winter super off-peak 10 a.m. to 3 p.m., Nov to Apr; up to $120 a year | aps.com Energy Saving Tips (search) | confirmed | |
| Hum without spinning: failed capacitor or jam (Angi) | not re-searched (budget) | kept, already hedged ("often") | general troubleshooting, no number or rule |
| Symptom table causes (bearings, shaft seal, suction air leak, overheating) | not re-searched | kept, hedged ("common causes") | general, safety advice consistent with rules |
| Angi repair $100 to $700, near $350; seal $100 to $250; bearings $150 to $350; motor repair $200 to $500; motor replacement $350 to $700 | Angi 2026 pump repair (search) | confirmed | |
| HomeGuide motor repair $50 to $300 | homeguide.com pool repair cost (search) | confirmed | |
| Angi new pump avg $1,300, most $700 to $4,000; variable speed $800 to $2,500 | Angi 2026 pump replacement (search) | confirmed | |
| DOE: 1.15 to 5 THP motors from Sept 29 2025 need variable speed control | energy.gov / Federal Register (search) | confirmed | |
| April 2026 policy delays enforcement for "some small motors made before March 26, 2029" | energy.gov GC enforcement policy (search) | corrected | made precise: small motors 0.5 to under 1.15 THP, compliance Sept 28 2027, enforcement held off for those built before March 26 2029 |
| DOE Building America guide: variable speed can use less energy | energy.gov guide (search) | confirmed | |
| ADWR recommends limiting pump run time | azwater.gov fact sheet (search) | confirmed | ADWR says no more than 3 hours a day; page wording is softer, fine |
| WMIDD supplies electricity in Wellton | research 13 | confirmed | |
| NWS: about 118 days at 100+, late April to early October, about 25 days at 110+ | research (NWS normals) | confirmed | |
| NOAA dust peak late July and early August for Yuma | coordinator note | corrected | same rewrite as equipment page |
| R-6 name and exclusions | ROC (search) | confirmed | |

Totals: 20 claims checked, 15 confirmed, 2 corrected, 0 softened, 1 removed, 2 kept as hedged general troubleshooting without a fresh search (the FAQ count stays at 5).

## Overall
67 claims checked: 46 confirmed, 9 corrected, 6 softened, 4 removed, 2 hedged general claims kept without a re-search. Searches: 23.
