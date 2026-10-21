# Yuma Pool Cleaning Pro (yumapoolcleaningpro.com): PLAYBOOK 2.0 REBUILD. INSTRUCTIONS FOR CLAUDE CODE

You are rebuilding a LIVE static lead-generation website for Maurice Johnson by running
Dominic & Dalton's Website Builder Prompt Playbook 2.0 (PLAYBOOK.md), Prompts 1 to 20, in full.
The site is live and indexed, so the rebuild must keep every URL Google knows.
(This repo is named arizona-pool-cleaning-pro, but it is the Yuma site.)

## RUN STRAIGHT THROUGH. DO NOT STOP.
Maurice is not watching this session and cannot approve anything. Do NOT pause at the end of each
playbook phase, do NOT ask "continue?", do NOT wait for input. Make reasonable decisions yourself,
write them down in docs/decisions.md, and keep going until Prompt 20 is finished and every check
below passes. Commit and push the `build` branch after each phase so work is never lost. The only
reason to stop early is if something would require paying money, deploying, merging to main, or
changing a repository other than this one.

## Source files (read all of them first)
- INTAKE.md: the facts. It wins over anything else. UNKNOWN means leave it off the site.
- PLAYBOOK.md: the playbook (Operating Rules, then Prompts 1 to 20). It was written for GHL AI
  Studio; apply its rules and its 20 steps to this static build system.
- keywords/Yuma-Pool-Keywords.xlsx: Ubersuggest, United States, pulled Oct 20 2026. 122 unique
  keywords, 12 seed tabs (each row typed Suggestion or Question) plus an ALL tab. Every Yuma-area
  keyword must be assigned to a page as a target or supporting keyword, or listed in
  docs/keyword-plan.md as deliberately unused with a one-line reason. "Near me" and national terms
  ("how much is pool maintenance" 720, "pool maintenance schedule" 480) are national volume:
  supporting keywords or guide targets only. Rows about other cities (San Diego, Gilbert, Queen
  Creek, San Tan Valley, San Luis Obispo, Kingman, Wickenburg, Sun City, California towns,
  "pool pump repair tucson"), rows naming a specific company ("yuma pro pool service", "crystal
  clear pool service yuma az"), public-pool searches ("somerton pool hours", and check "yuma pool",
  "wellton pool", "somerton az pool" yourself) and job searches ("pool repair jobs") go in the
  unused list.
- The current live site (this repo's main branch): /, /pool-service, /pool-cleaning, /about/,
  /contact/, /faq/, /privacy-policy.html, /terms.html. Read every page before writing. Keep useful
  verified facts, re-verify them on the web, but do NOT copy its paragraphs: every page is written
  fresh. Reuse its photos in images/ first.

## Copy the build system from Tucson Pool Cleaning Pro (NOT its words)
The repository dominionsoundmusic-create/tucson-pool-cleaning-pro, branch `main`, holds a finished
Playbook 2.0 rebuild of the sister Tucson site (merged and live Oct 20 2026). Clone it and copy its
BUILD SYSTEM: build.py, scripts/check.py, scripts/similarity.py, the old-URL check script,
src/templates/, src/static/css/site.css and JS, the macros (img, faqs, sources, disclosure), the
site.json structure, netlify.toml (publish = "dist") and the docs/ document set as a pattern. Keep
its full-width layout, centered card rows, left-to-right footer rows and the Google Translate EN/ES
toggle. Adapt every Tucson value to Yuma.
NEVER copy page text, paragraphs, FAQs or sentence runs from Tucson, Phoenix or any other site. No
Tucson-metro or Phoenix-metro places, no Tucson Water, TEP, Pima County or Maricopa County facts.
Research Yuma equivalents instead: Arizona Public Service (APS) serves Yuma for electricity (verify
which areas), the City of Yuma water utility and each nearby town's water provider and their
hardness (Yuma's water comes from the Colorado River and is very hard: verify the current number),
City of Yuma and Yuma County rules on draining pools and backwash, extreme summer heat (Yuma is one
of the hottest and sunniest places in the US: verify with NWS), very high evaporation, UV and
stabilizer, dust storms, calcium scale, and the winter visitor (snowbird) season, when many pools
sit unused for months.
Keep the speed fix exactly: WebP 480/800/1200/1600/1920 srcset, preloaded hero with fetchpriority
high, self-hosted woff2 font, the site CSS inlined in a <style> block instead of a render-blocking
stylesheet link, GA4 (G-STXQ0LYCST) loaded only on first scroll/click/keypress/touch or 3.5 seconds
after load, and any YouTube video click-to-play (thumbnail plus play button, iframe only on click).

## URLs: keep every live URL (this is a rebuild of an indexed site)
Every URL in main's sitemap.xml and every page file on main must still resolve on the new site,
either as a rebuilt page at the SAME path or a 301 to the closest new page (record each in
docs/decisions.md). That includes /, /about/, /contact/, /faq/, /pool-service, /pool-cleaning (both
with and without .html), /privacy-policy.html and /terms.html. Keep every existing _redirects rule
that still makes sense and copy _redirects into dist/. If you build a real page at a path an old
rule redirects (for example /pool-maintenance/ or /pool-equipment-repair/), remove that rule. Run
the old-URL check script and record the result in docs/qa.md.

## Pages to build (decide the exact list from the keywords, then follow it)
- Core: home (target "pool service yuma az" 260, "yuma pool service" 260 and "pool service yuma"
  210), services overview, service areas overview, how it works, about, FAQ, contact (a phone
  page), privacy, terms, 404.
- Service pages: one per real service with Yuma or national question demand. At least: weekly pool
  service (keep /pool-service), pool cleaning (keep /pool-cleaning, "pool cleaning yuma" 40), pool
  repair ("pool repair yuma" 40), pool pump repair, green pool cleanup, pool tile cleaning and
  calcium scale, plus pool equipment repair if the data supports it.
- Guide pages for the strongest question keywords, each researched and sourced: how much pool
  maintenance and pool service cost ("how much is pool maintenance" 720, "how much is a pool service
  per month" 30; cite published, sourced ranges and say real quotes vary), a Yuma pool maintenance
  schedule ("pool maintenance schedule" 480: summer heat, monsoon dust, snowbird months), "my pool is
  green, how do I fix it" (110), and any other strong question cluster (for example "is a pool
  service worth it", "how often do pool pumps need to be replaced").
- Town pages: Maurice's rule is ANY town with 10 or more searches a month for a POOL SERVICE
  keyword gets its own page. Check Fortuna Foothills, Somerton, San Luis, Wellton and Gadsden in
  the data yourself. Public-pool searches (hours, "town pool") and other places named San Luis or
  San Luis Obispo do not count. If no town qualifies, build no town pages and cover those towns on
  the service areas page instead, honestly. Record the exact keyword and volume per town (or that
  it has none) in SERVICES.md.
- Write SERVICES.md (every page, URL, target keyword with volume and SEO difficulty) and
  docs/keyword-plan.md before writing pages. Yuma is a small market: honest, shorter pages beat
  padding.

## Hard rules for every page
1. Never "our technicians", "our trucks", "we clean", "we repair", "we are licensed/insured" or
   anything implying the line does pool work.
2. Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business,
   team members, job counts, guarantees, awards or statistics. Research and state accurately what
   Arizona requires (the Registrar of Contractors licenses pool contractors for some work; check
   which work needs a license and say so correctly), and tell readers how to look a company up on
   the Arizona ROC search.
3. Never name a specific pool company.
4. Only Yuma County, Arizona places. No California, no Mexico, no other Arizona metros, no other
   states.
5. No em dashes or en dashes in visible copy (except the Duplantis credit). No eyebrow labels.
   American spelling.
6. No DIY chemical-mixing instructions beyond safe basics, no electrical or gas work. Safety first:
   never mix pool chemicals, keep children away from an unfenced pool, a pool heater gas smell means
   leave the area and call the gas utility or 911.
7. No prices presented as the line's prices. Cost guides cite published, sourced ranges and say
   real quotes vary.
8. Every page except privacy, terms and 404 has 3 to 6 FAQs written the way people ask (use the
   Question rows), rendered visibly AND as FAQPage JSON-LD in the page's single JSON-LD graph.
9. Every page has a full-width hero image plus at least two in-body images, each with filename,
   alt, width, height and loading="lazy" (hero eager). Reuse this repo's images first. One photo
   may fill several spots across the site, but never twice on the same page.
10. Facts must be real and current. Research each page on the web and cite every source in the
    page's sources list. If you cannot verify a fact, leave it out.
11. Each page is written for its own keyword. Never reuse paragraphs between pages with names
    swapped. Measure: Jaccard similarity on 5-word shingles between every pair of pages of the
    same type, and every Yuma page against every Tucson page and every Phoenix page; any pair above
    15% gets rewritten. Record the numbers in docs/qa.md.
12. The referral disclosure appears on every page (wording in INTAKE.md).
13. Banned phrases: "your trusted partner", "one-stop solution", "look no further", "unmatched
    excellence", "we've got you covered", plus the WORDS TO AVOID in INTAKE.md.
14. Mark every page with the HTML comment `dwdp:handwritten 2026-10-20` in the first 4KB.

## Design (Maurice's standing rules, check each one)
- Header/menu bar in a real brand color (teal from the logo), never dull gray. Phone visible with
  tap-to-call. EN/ES Google Translate toggle in the header on every page, in brand colors.
- Hero stretches edge to edge on every page: full-strength photo, dark left-to-right fade behind
  the headline, logo/headline/buttons aligned to the left rail at 1440, 1920 and 2560 wide. Hero
  stays above the fold (max-height about 700px) with the call button visible.
- Body text, photos and cards run FULL WIDTH on the rail. Never box text into a narrow center strip.
- Mostly WHITE sections broken by occasional bold color bands (hero, white, teal band, white, a
  second band in desert gold or deep teal-navy). Never pale off-white tints. Never every section
  tinted.
- No white text or white boxes on white. Every card, box and button has clear contrast.
- Card rows: 3 / 2 / 1 columns, any short last row CENTERED. Footer links and towns run left to
  right in rows.
- Logo: keep the site's existing logo.svg unless it is broken; favicon too.

## Before you finish (all must pass)
- `python3 build.py` then `python3 scripts/check.py`: 0 errors.
- Every old URL resolves on the built site or has a 301 in dist/_redirects (script, result in
  docs/qa.md).
- Grep the built site for: em/en dashes in visible text (except the Duplantis credit), "we clean",
  "we repair", "our technicians", "licensed and insured", "background checked", "free estimate",
  "same-day", "500+", "starting at", "Tucson", "Phoenix", "Scottsdale", "Mesa", "Gilbert",
  "Pima", "Maricopa", "San Diego", "California", "El Centro", "Winterhaven", "Houston", "Texas",
  "(520)", "(623)", "(903)", "903-636". Fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px wide.
- Independent fact-check: start separate sub-agents that did not write the pages, have them check
  every factual claim and source on every page, and fix what they find. Record it in
  docs/fact-check.md. Never say "fact-checked" unless this was actually run.
- docs/image-list.md lists every image still needed: File name, Size, then an Artistly prompt
  (bright, clearly visible, Yuma-area homes and backyard pools, low Sonoran desert landscaping,
  no lake, no river, no text, no logos, no recognizable faces, "wide cinematic landscape shot,
  subject positioned on right third of frame, well lit"). Missing images must never show as broken:
  pages use an existing photo until the new one arrives.

## Git
- Work on the branch `build`. Commit as you go with clear messages and push `build` after each
  phase.
- When finished, open a pull request from `build` to `main` so Netlify makes a deploy preview, but
  do NOT merge it.
- Do NOT merge to main, do NOT push to main, do NOT deploy, do NOT touch Netlify settings, do NOT
  pay for anything. Maurice decides when it goes live.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built (count by type), checks passed, duplication range, fact-check result, how many images
need Artistly, and the one thing Maurice must do next.
