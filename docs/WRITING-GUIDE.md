# Writing guide for yumapoolcleaningpro.com pages (Playbook 2.0 rebuild, Oct 21 2026)

Repo: /home/user/arizona-pool-cleaning-pro (branch `build`). Read these first, in full:
1. `CLAUDE.md` (the hard rules) and `INTAKE.md` (the facts; it wins over everything; read "WHAT THE
   BUSINESS ACTUALLY IS" twice).
2. `SERVICES.md` and `docs/keyword-plan.md` (your page's URL, TARGET keyword and supporting keywords,
   including the Question rows to turn into FAQs).
3. The research fact bank in `docs/research/`: `water-utilities-rules.md`, `climate-seasons.md`, `towns.md`,
   `licensing-safety.md`, `costs-equipment.md`. These facts were verified from official or named sources by
   search; use them and cite the source URL each fact gives. Respect each file's "Could NOT verify" list:
   those claims stay off the site.
4. `src/data/site.json` (names and URLs of services, guides and areas) and `src/templates/macros.html`.
5. STRUCTURE MODELS ONLY: the finished sister site Tucson Pool Cleaning Pro, built with the same system:
   `/home/user/dominionsoundmusic-create/tucson-pool-cleaning-pro/src/pages/pool-pump-repair.html` (service),
   `.../pool-service-cost.html` (guide), `.../index.html` (home), `.../service-areas.html`. Match their depth,
   section rhythm and component use. NEVER copy their wording, sentences, FAQs, headings or facts (they are
   about Tucson). `scripts/similarity.py` compares every Yuma page with every Tucson page and every Phoenix page
   and FAILS on any shared run of 8 words or a Jaccard above 15%. Write from scratch, in your own sentences.
6. The old Yuma page for your URL in `docs/old-site/` (if any), for research leads only. Its claims ("175 days
   above 100 degrees", "hottest city in Arizona", "chemicals are included", one flat monthly price, "same
   technician", "fixes it on site", "30 to 50 percent more chlorine", "population nearly doubles") are FALSE,
   UNVERIFIED or banned. Never copy or lightly reword its text.

## The business, in one paragraph
Yuma Pool Cleaning Pro is a free phone line and website, NOT a pool company. An automated assistant answers
(928) 615-5224 any hour, asks briefly what is going on with the pool, then transfers the call to an
independent, locally owned Yuma-area pool service company. That company hears a short summary before it picks
up. If it cannot answer, the caller's name, callback number, area and pool problem are passed along for a call
back. The company looks at the pool, quotes, does the work and is paid directly by the customer. The line never
cleans, repairs, quotes or schedules anything, holds no license, never charges the caller, and may be paid a
referral fee by the companies. Write "the pool company you are put through to", "the pool service company", "a
careful pool technician". Never "our technicians", "our trucks", "we clean", "we repair", "we are
licensed/insured", "we'll send someone". Never say the connected companies are licensed, insured, certified,
rated or reviewed. Tell readers to ASK for the company's Arizona ROC license number and look it up on the ROC
contractor search (https://roc.az.gov/contractor-search). Never name any pool company. Avoid equipment brand
names. Never write the phone number by hand: use `{{ site.business.phone_display }}` (tel link:
`tel:{{ site.business.phone_tel }}`).

## Hard rules (scripts/check.py and scripts/grep_check.py enforce most of them)
- No em dashes or en dashes anywhere (copy, titles, descriptions, FAQs, alt text). Use commas, colons, periods
  or "to" ("4 to 7 p.m."). American spelling. No eyebrow labels or badges.
- Only Yuma County, Arizona places: Yuma, Fortuna Foothills ("the Foothills"), Somerton, San Luis, Wellton,
  Gadsden, Yuma County, and Yuma-area features named in docs/research (Colorado River, Gila Mountains, Yuma
  Valley, Marine Corps Air Station Yuma, Yuma Proving Ground, Interstate 8, U.S. 95). NEVER any
  other Arizona metro or town (no Phoenix, Tucson, Scottsdale, Mesa, Gilbert, Kingman, Wickenburg), never Pima
  or Maricopa County, never another state or country: no California, no El Centro, no Winterhaven, no Mexico
  (say "the international border" if you must), no Texas. Do not compare Yuma with other cities. Never write
  "the Valley". Utilities: electricity is Arizona Public Service (APS) for Yuma, Somerton and San Luis per the
  APS map, and the Wellton-Mohawk Irrigation and Drainage District in Wellton; for the Foothills and Gadsden say
  "APS or another provider, depending on the address" or "your electric bill names your provider". Gas is
  Southwest Gas. Never mention the ROC's street address; use its website and toll-free 1-877-692-9762.
- Never invent licenses, insurance, reviews, ratings, prices, years in business, team members, job counts,
  statistics, response times, guarantees or awards. Public statistics are fine with the source named and listed.
  Prices: only published national ranges with the publisher named on the page and a note that real quotes vary;
  never present a price as the line's price. There are no Yuma-specific published prices: do not imply any.
- Banned (checker fails): "free estimate(s)", "same-day", "same day", "guarantee(d)", "best price", "cheapest",
  "top-rated", "years of experience", "#1", "number one", "licensed and insured", "background checked",
  "chemicals included", "flat monthly price", "starting at" (avoid the phrase entirely, even innocently),
  "500+", "5-star", "your trusted partner", "one-stop solution", "look no further", "unmatched excellence",
  "we've got you covered", response-time promises ("within 2 hours"). The grep check also bans the word
  "Mesa" anywhere, so never write "Yuma Mesa".
- Safety first, no DIY beyond safe basics:
  - Never give chemical-mixing or dosing instructions (no "add X pounds of shock", no acid washing steps, no
    acid dilution). Say plainly: never mix pool chemicals with each other (CDC), keep them in original
    containers, dry, cool, shaded and secured away from children and pets, follow the label, and leave acid
    work to a professional.
  - No electrical work (motors, wiring, lights, breakers beyond resetting a tripped GFCI or breaker once; a
    breaker that trips again means leave it off and call), no gas work. Pool heater gas smell: leave the area
    right away, do not use switches, flames or anything that could spark, and from a safe distance call 911 and
    Southwest Gas at 877-860-6020.
  - Children: keep them away from an unfenced or uncovered pool, never leave a child unsupervised near water,
    and a green or murky pool is a drowning hazard because the bottom cannot be seen. CDC: drowning is the
    number one cause of death for children ages 1 to 4.
  - Safe homeowner checks only: skimmer and pump baskets, the filter pressure gauge reading, the timer or
    automation schedule, water level at the skimmer, visible leaks or drips at the equipment pad, a tripped
    GFCI or breaker (reset once), debris around the equipment, testing water with a home test kit or strips,
    the bucket test for evaporation.
- Every fact that is not common knowledge carries a source in the page's Sources list with a real URL. If you
  cannot verify it, leave it out.

## Key shared facts (verified; see docs/research/ for details and URLs)
- City of Yuma water: Colorado River water treated at the Main Street and Agua Viva plants. The city's Water
  FAQs call it hard: 18 to 22 grains per gallon (310 to 380 mg/L). San Luis: groundwater from ten wells.
  Wellton: Colorado River water through the Wellton-Mohawk district canals (2018 report). Somerton runs its own
  utility (source not confirmed). Fortuna Foothills: Foothills Utilities (formerly Far West Water & Sewer).
  Never give a hardness number for any place but the City of Yuma.
- NWS Phoenix normals for Yuma (1991 to 2020): about 118 days a year at or above 100 F (average first April
  25, last October 6), about 25 days at or above 110 F, July average high 106.7 F, 3.28 inches of rain a year,
  record 124 F on July 28, 1995, frost about 0.1 days a year. NOT "175 days", NOT "hottest city in Arizona".
- Sunshine: Visit Yuma says Yuma gets about 91% of possible daylight hours (4,055 of 4,456) and cites Guinness
  as naming it the sunniest place on earth; attribute it to Visit Yuma.
- Evaporation: EPA WaterSense says an uncovered pool can lose 12,000 to 31,000 gallons a year to evaporation
  and a cover can cut that by up to 95%. AZMET Yuma reference evapotranspiration is about 80 inches a year
  (that is a crop-water figure, not a pool figure: describe it carefully or not at all).
- Monsoon season June 15 to September 30 (NWS). NOAA names Yuma as a dust storm area, peak late July and early
  August. UV index 11 or more is "extreme" (EPA/NWS scale).
- Winter visitors: a 2017 to 2018 Visit Yuma / Arizona Office of Tourism study counted about 71,000 winter
  visitors staying 30 days or more, December to May. Yuma County says the population grows by about 90,000 in
  winter. Visit Yuma says Fortuna Foothills is largely winter visitors. Many pools sit unused through summer
  while their owners are away: that is when they turn.
- CDC home pools: pH 7.0 to 7.8; free chlorine at least 1 ppm, at least 2 ppm with cyanuric acid (stabilizer);
  sunlight breaks chlorine down; never mix chemicals.
- APS time-of-use: on-peak 4 to 7 p.m. weekdays year-round on current plans (older plans 3 to 8 p.m.); winter
  super off-peak 10 a.m. to 3 p.m. weekdays (November to April). APS says run the pool pump off-peak and that
  running it in the winter super off-peak window can save up to $120 a year.
- Draining in the City of Yuma: call City of Yuma Utilities (928-373-4500) first (City Code 191-02 needs the
  Director of Utilities' authorization for pool drainage to the sewer); the city's stormwater page says use the
  private sewer cleanout on your own property (never a public manhole), stop chlorine 48 hours before, drain
  slowly at low-use hours, and never let water run into the street. Unincorporated Yuma County (the Foothills,
  Gadsden): chlorine at or below 1 ppm before release, saltwater pools only to the sanitary sewer, no permanent
  connection to a storm drain or wash.
- Barriers: City of Yuma code 154-15.05: fence or wall at least 5 feet high, openings no larger than 4 inches,
  self-closing self-latching gates; City of Yuma adopted the 2018 International Swimming Pool and Spa Code.
  A.R.S. 36-1681 statewide basics (5 feet, 54 inch latch, gates open outward).
- Green pools: Yuma County Public Health calls green, unmaintained pools a major breeding source for West Nile
  mosquitoes; report them through the county service request page or Vector Control at (928) 317-4584.
- ROC: R-6 Residential Swimming Pool Service and Repair covers servicing and minor repairs; it excludes gas
  lines, electrical work beyond the first disconnect, potable water plumbing connections, and complete plaster
  or pebble replacement. B-5 / B-6 build and repair pools. No official statement on cleaning only: say the ROC
  does not spell it out, ask. Contractor search shows status, classification, complaints and bond, not
  insurance; the ROC does not require insurance except workers' compensation.
- DOE: pool pump motors 1.15 to 5 total horsepower made on or after Sep 29 2025 must offer variable speed;
  smaller motors from Sep 28 2027, enforcement delayed for small motors made before March 26 2029 (April 2026
  policy). Nobody has to replace a working pump.
- CPSC: GFCI protection for underwater lights, test GFCIs monthly; barriers, supervision, drain covers.

## Voice
Plain, specific, warm, Yuma-local. Second person. Short paragraphs, roughly 7th to 8th grade reading level;
explain a technical word the first time (cyanuric acid, total dissolved solids, calcium hardness). Explain why.
Remember the Spanish toggle: write sentences that machine-translate well (no idioms, no puns). No filler, no
superlatives, no keyword stuffing. The target keyword appears naturally in the title, H1, first paragraph, one
H2 and the meta description. Yuma is a small market: honest and useful beats long. Pages should be
substantial but never padded.

## Page file format
`src/pages/<file>.html` with YAML front matter, then `{% block content %}...{% endblock %}`. Folder URLs need
no `url:` (file `src/pages/pool-repair.html` becomes /pool-repair/). The two flat live pages use `url:
"/pool-service"` and `url: "/pool-cleaning"`.

```yaml
---
type: service            # service | guide | page | about | contact
url: "/pool-service"     # ONLY for the flat pages /pool-service and /pool-cleaning
title: "..."             # 50 to 65 chars, unique, keyword near the front
description: "..."       # 120 to 160 chars, unique, no dashes
h1: "..."                # one H1, unique
crumb: "..."
keyword: "pool repair yuma"
published: "2026-10-21"  # guides only
hero:
  image: pool-repair-hero.jpg    # PLANNED 1920x1080 photo (see Images)
  alt: "..."
  desc: "Artistly prompt for the planned photo."
  fallback: pool/hero-2.jpg      # existing photo shown until the planned one exists (given in your brief)
  fallback_alt: "..."            # accurate alt for the fallback photo
  lead: "One or two sentences under the H1."
  secondary_label: "..."         # optional: a real page or an in-page anchor, never a form
  secondary_href: "/..."
schema_service:          # service pages
  name: "Free connection to a local pool repair company in Yuma, Arizona"
  type: "Pool repair referral"
cta_title: "..."         # short, specific to the page
faqs:                    # 3 to 6 (never more), phrased the way people ask (use the Question rows)
  - q: "..."
    a: "<p>...</p>"
---
```
Quote YAML strings that contain a colon. Inside FAQ answers use `&amp;` or the word "and" for "&".

## Building blocks (existing classes only; do not edit CSS, templates, build.py, scripts or site.json)
- Reading column: `<section class="prose">...</section>`. Text runs full width between the page rails; never
  add wrappers that narrow it.
- Color band: `<section class="band band--tint"><div class="wide">...</div></section>`. The build turns the
  first into a bold teal band (white text) and the second into a desert gold band (dark text). Use ONE or TWO
  per page, with white prose sections between; never two bands in a row; do not end your content with a band
  (the FAQ block and the call band follow automatically).
- Two columns, text and photo: inside `.prose`, `<div class="split"><div>text</div>{{ img(...) }}</div>`.
- `<ol class="steps">` numbered process; `<ul class="checks">` checklist; `<div class="grid-2">` /
  `<div class="grid-3">` of `<div class="panel">` (add `panel--do` / `panel--dont`); `<ul class="facts">` of
  `<li><strong>label</strong>text</li>`; tables in `<div class="table-wrap"><table>` with `<caption
  class="sr">`, `<thead>`, `scope` on th; `<div class="note">` callout, `<div class="note note--orange">`
  warning.
- Macros: `{{ m.how_it_works_short() }}`, `{{ m.disclosure() }}`, `{{ m.license_check() }}`,
  `{{ m.call_box('text') }}`, `{{ m.service_cards(['slug', ...]) }}`, `{{ m.guide_cards(['slug']) }}`,
  `{{ m.area_pills() }}`, `{{ m.related(['slug','guide:slug'], 'Title') }}`,
  `{{ m.sources([{'label': '...', 'url': '...'}, ...]) }}` (always last, inside the last prose section).
  Service slugs: pool-service, pool-cleaning, pool-repair, pool-pump-repair, pool-equipment-repair,
  green-pool-cleanup, pool-tile-cleaning. Guide slugs: pool-maintenance-cost, pool-maintenance-schedule,
  my-pool-is-green, is-a-pool-service-worth-it.
- Links: use the `url` values in site.json exactly: `/pool-service`, `/pool-cleaning` (no slash, flat pages),
  `/pool-repair/`, `/pool-pump-repair/`, `/pool-equipment-repair/`, `/green-pool-cleanup/`,
  `/pool-tile-cleaning/`, `/pool-maintenance-cost/`, `/yuma-pool-maintenance-schedule/`, `/my-pool-is-green/`,
  `/is-a-pool-service-worth-it/`, core `/how-it-works/`, `/service-areas/` (towns: `/service-areas/#fortuna-foothills`,
  `#somerton`, `#san-luis`, `#wellton`, `#gadsden`, `#yuma`), `/services/`, `/about/`, `/faq/`, `/contact/`. Link to
  3 or more related pages naturally in the copy.

## Images
Call: `{{ img('file.jpg', 'alt', 1200, 800, desc='prompt', fallback='pool/x.jpg', fallback_alt='...') }}`.
An existing photo used directly needs no desc/fallback: `{{ img('pool/chem-wide.jpg', 'alt', 1200, 500) }}`.
Every content page: a hero plus at least two in-body images; NO photo twice on one page (count the hero or its
fallback, and the card images of any `m.service_cards` you include; `pool/hero-1.jpg` and
`pool/hero-1-wide.jpg` are the same scene and count as one photo). Card images: pool-service skim-wide,
pool-cleaning brush-wide, pool-repair repair-wide, pool-pump-repair equip-wide, pool-equipment-repair
dusk-wide, green-pool-cleanup green-wide, pool-tile-cleaning hero-3-wide. Alt text must describe what the
photo really shows and must not imply a worker is from the line.

Existing photos in src/static/images (bright desert backyards or pool close-ups), with sizes:
- `pool/hero-1.jpg` 1920x800 (curved pool, stucco house with covered patio, lounge chairs, desert plants, a
  saguaro, rocky mountains), `pool/hero-2.jpg` 1920x800 (free-form turquoise pool, flagstone deck, boulders,
  covered patio with dining table, palms, cacti, mountains), `pool/hero-3.jpg` 1920x800 (long rectangular pool
  with white lounge chairs, palms, desert trees, boulders, distant mountains), `img-01.jpg` 1344x768 (aerial of
  a kidney-shaped pool with a saguaro, agaves, red boulders and open desert beyond the wall).
- 1200x500 wide crops: `pool/hero-1-wide.jpg`, `pool/hero-2-wide.jpg`, `pool/hero-3-wide.jpg` (same scenes),
  `pool/brush-wide.jpg` (hand pushing a blue brush under clear water), `pool/chem-wide.jpg` (two white chemical
  jugs and a test cup on a deck at sunset), `pool/dusk-wide.jpg` (lit pool at dusk, string lights, stone patio,
  cacti), `pool/equip-wide.jpg` (pump and plumbing beside a tall filter tank, stucco wall), `pool/green-wide.jpg`
  (neglected green pool with leaves, block wall), `pool/repair-wide.jpg` (two hands turning a wrench on an old
  pump, workshop), `pool/skim-wide.jpg` (a man in a pool skimming with a leaf net, saguaro behind the wall,
  face not shown), `pool/test-wide.jpg` (hand holding a water sample vial at the surface), `pool/vac-wide.jpg`
  (robotic cleaner on a sunlit pool floor).
Do not say a photo was taken in Yuma.

Planned new photos (Maurice generates them in Artistly later). Each needs a unique descriptive filename, a
`desc=` prompt and a `fallback=` existing photo. Prompt style (CLAUDE.md): start with "Wide cinematic landscape
shot, subject positioned on right third of frame, well lit," then a specific, bright, realistic Yuma-area scene
(single-story stucco homes in tan, sand or white with flat or low tile roofs, block walls, low Sonoran desert
landscaping with crushed gravel, palo verde and mesquite trees, ocotillo, agave, a few date or fan palms, bare
rocky desert mountains in the distance, clear blue sky), then "realistic photo, no lake, no river, no text, no
logos, no house numbers, no recognizable faces". No saguaros in new prompts (they are rare in Yuma).
- Hero = PLANNED `<slug>-hero.jpg`, 1920x1080, with the fallback given in your brief. In-body: existing photos;
  at most ONE planned in-body photo per page (1200x800, with an existing fallback that is not otherwise on the
  page).

## Content each page needs
Service and guide pages (Prompt 9): what it is; who it is for; common problems; what a careful pool technician
does and why; what to expect; options; Yuma-specific context (verified only: heat, sun, hard water, dust,
winter visitor months, APS hours, local rules); safe homeowner checks where relevant; what to ask; related
pages; 3 to 6 FAQs; at least one distinctive design treatment (symptom table, decision panels, timeline,
checklist, comparison table); `m.how_it_works_short()` or a short plain explanation of the line plus
`m.disclosure()`; `m.license_check()` where repair work is discussed. Roughly 1,100 to 1,700 words of
page-specific copy (a small market: no padding). Sources list at the end.

## Research standard
- Use the fact bank first. For anything page-specific, research on the web BEFORE writing: WebFetch and curl
  are blocked for most hosts; use WebSearch (load it with ToolSearch "select:WebSearch"; mode "standard"),
  restricted with allowed_domains to official domains (yumaaz.gov, yumacountyaz.gov, roc.az.gov, azleg.gov,
  azwater.gov, weather.gov, census.gov, aps.com, swgas.com, energy.gov, cdc.gov, cpsc.gov, epa.gov,
  extension.arizona.edu, arizona.edu, and the named cost publishers). Cite the official URL whose content the
  search showed. Your search budget is given in your brief; stay within it.
- Every number, date, rule, phone number, fee and named program comes from a source you saw; that source goes
  in the Sources list with its real URL. If you cannot verify it, leave it out.
- Shared facts (hard water, heat days, monsoon, ROC): say them in your own words, only where they matter to that
  page, never the same paragraph twice across pages.

## Validation (from the repo root; NEVER a plain `python3 build.py`, it writes dist/ and docs/)
```
python3 build.py --out /tmp/claude-0/<your-name>/dist
python3 scripts/check.py --dist /tmp/claude-0/<your-name>/dist --skip-links --only <your page URL>
python3 scripts/similarity.py --dist /tmp/claude-0/<your-name>/dist \
  --other /home/user/dominionsoundmusic-create/tucson-pool-cleaning-pro/dist \
  --other /home/user/dominionsoundmusic-create/phoenix-pool-cleaning-pro/dist --only <your page URL as similarity prints it>
python3 scripts/grep_check.py --dist /tmp/claude-0/<your-name>/dist
```
(similarity prints flat pages as `/pool-service.html`, folder pages as `/pool-repair/`, home as `/`.)
build.py may print FAILED for other writers' half-finished pages; ignore those, fix your own. grep_check covers
the whole dist; only fix hits in your own pages. Fix every ERROR and FAIL for your pages. A WARN about word
count under 1500 (which includes the template) on a service or guide page means the page may be thin: add
substance, not filler. Do not edit shared files or anyone else's pages. Do not commit or push.

When done, report: files written, word counts, any fact you could not verify and left out, and searches used.
