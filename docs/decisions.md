# Decisions log (Yuma Playbook 2.0 rebuild, Oct 21 2026)

Maurice was not available to approve anything during this run (CLAUDE.md: run straight through). Each
decision below was made from INTAKE.md, CLAUDE.md, the keyword data and the live site, and can be reversed.

## Build system and structure
1. **Build system copied from Tucson Pool Cleaning Pro (main), words not copied.** build.py, scripts/check.py,
   similarity.py, check_old_urls.py, grep_check.py, keyword_plan.py, responsive_check.js, functional_check.js,
   the Jinja templates and macros, site.css, site.js, the self-hosted Inter woff2, the site.json structure and
   netlify.toml (`publish = "dist"`). Every Tucson value was changed to Yuma, and every shared template
   sentence (call band, how-it-works strip, call box, license note, disclosure, 404, legal pages) was written
   fresh. similarity.py compares every Yuma page with every Tucson and every Phoenix page.
2. **Speed fix.** WebP srcset 480/800/1200/1600/1920, preloaded hero with fetchpriority high, self-hosted woff2
   font. The Tucson build still linked /css/site.css and loaded GA4 at once; this build inlines the CSS in a
   `<style>` block and loads GA4 only on the first scroll, click, key press or touch, or 3.5 seconds after
   load, as CLAUDE.md asks. A YouTube click-to-play macro is ready; no video is on the site yet.
3. **Old live site moved to docs/old-site/** (page files, sitemap, robots, _redirects, favicons) and its photos
   to src/static/images/ at the same public paths, so old image URLs still resolve. docs/old-site/retired-urls.txt
   lists the 88 page files main deleted in Sep 2026 (templated city pages, blog posts), taken from git history,
   so check_old_urls.py also tests those.
4. **URLs kept.** /, /about/, /contact/, /faq/, /privacy-policy.html and /terms.html are rebuilt at the same
   paths. /pool-service and /pool-cleaning were flat files on main and are flat files again
   (dist/pool-service.html, dist/pool-cleaning.html), so both work with and without .html. New pages use
   folder URLs.
5. **Redirects (src/static/_redirects, copied to dist/).** Every Sep 2026 rule kept. Re-pointed to the closer
   new page: /algae-treatment/ to /green-pool-cleanup/; /pool-cleaning-near-me/ to /pool-cleaning;
   /weekly-pool-cleaning/ to /pool-service; blog posts on equipment and on saltwater pools to
   /pool-equipment-repair/, on weekly service cost to /pool-maintenance-cost/, on algae and green water to
   /my-pool-is-green/. **/pool-equipment-repair/ is a real page again, so its two old rules were removed**;
   its nine retired city pages (with and without .html) now 301 to it one by one, because a wildcard would
   also match the real page.
6. **Phone only.** The old `yuma-pool-inquiry` Netlify form is retired; /contact/ is a phone page. The form
   posted to the page itself with no thank-you URL, so no redirect was needed. check.py fails any `<form>`.
7. **Phone number in one place.** (928) 615-5224 lives only in src/data/site.json.
8. **Kept from main:** GA4 G-STXQ0LYCST with the phone-tap event and the Facebook URL.
9. **No governing-law clause in the terms.** The Tucson terms name Texas law, but the Yuma grep list bans the
   word "Texas", and the old Yuma terms had no such clause. Maurice can add one later.

## Design
10. **Colors.** Header bar in logo teal, darkened to #0d6b60 so white menu text passes WCAG AA. Headings, the call
    band and the footer in the logo's deep teal-navy (#0f2e29, #0a1f1c). Call buttons in the logo's desert gold
    #f5c451 with dark text. First color band teal with white text, second band desert gold with dark text.
    White sections between bands; the FAQ block is white.
11. **Layout kept from Tucson:** full-width rail layout, centered card rows (3 / 2 / 1, short last row
    centered), footer rows left to right, EN/ES Google Translate toggle in the header.
12. **Logo and favicons** kept from the live site; an apple-touch-icon.png was rendered from favicon.svg.

## Pages and keywords (SERVICES.md, docs/keyword-plan.md)
13. **21 pages:** 10 core, 7 service, 4 guide, 0 town.
14. **Home** targets "pool service yuma az" (260), "yuma pool service" (260) and "pool service yuma" (210).
    /pool-service targets the weekly maintenance terms so it does not compete with the home page.
15. **Pool equipment repair gets its own page** (own seed tab, two equipment questions, old indexed URL with
    city pages); filters, heaters, heat pumps and salt cells are not pump work.
16. **Guides:** cost ("how much is pool maintenance" 720), Yuma maintenance schedule ("pool maintenance
    schedule" 480), "my pool is green how do i fix it" (110) and "is a pool service worth it" (10). The pump
    replacement question (20) is answered on the pump page rather than in a thin separate guide.
17. **No town pages.** No town has 10 searches a month for a pool service keyword (table in SERVICES.md).
    "wellton pool" (30) and "wellton az pool" (10) are public-pool searches: Wellton runs a town pool (the
    N.D. and Katie Kline Pool in its newsletters). "somerton pool hours" and "somerton az pool" likewise.
    "yuma pool" (590) and "pool yuma" (40) are unused: the City of Yuma runs four public pools and the file pairs
    the term with "yuma pool hours", so the intent is mostly a city pool.

## Writing, fact-check and QA
18. **Pages were written by eight separate writer agents** from docs/WRITING-GUIDE.md and the research files
    (docs/research/), and checked by five different fact-check agents that wrote nothing (docs/fact-check.md).
19. **Old false claims dropped:** "175 days above 100 degrees" (NWS normal is about 118), "hottest city in
    Arizona", "chemicals included", one flat monthly price, "same technician", on-site fixes, "30 to 50 percent
    more chlorine", "population nearly doubles". The live site's footer copyright is now Dominion Digital Group.
20. **Winter visitor figure.** The research file's "about 71,000 winter visitors" (2017 to 2018 ASU study) could
    not be found again; every page uses Yuma County's "about 90,000" instead.
21. **Hardness:** only the City of Yuma publishes a number (18 to 22 grains per gallon, 310 to 380 mg/L, Water
    FAQs). No figure is given for any other place.
22. **Electricity:** pages say the electric bill names the provider; APS is named for Yuma, Somerton and San Luis
    as its map labels them, and Wellton's power is the Wellton-Mohawk Irrigation and Drainage District.
23. **Tile cleaning states no price:** no cost guide publishes a pool tile or calcium removal price.
24. **NWS source labels** say "National Weather Service" without the office name, because the office is named
    after another city and the grep check bans that word.
25. **Shared license note** was reworded once more mid-build because its first wording shared runs with the
    Phoenix site; similarity.py drops it as template text.
26. **Browser QA ignores blocked third-party requests** (Google Analytics, Translate), which the sandbox cannot
    reach; every other console error still counts.

## Oct 29 2026: quote form added to /contact/
Maurice asked for a short quote form with a "What do you need?" dropdown so he gets a text with the
visitor's need. /contact/ now has the Netlify form `yuma-pool-contact` (fields name, phone, email,
city, need, message; honeypot bot-field) posting to the new noindex /contact/thanks/ page. The
Netlify function netlify/functions/submission-created.mjs (copied unchanged) sends the text and
email. check.py now requires that form on /contact/ and still fails a form on any other page; the
thanks page is exempt from the FAQ and image rules like 404. The "phone only" wording on contact,
about, how it works, privacy and terms was rewritten; the call stays the main way in.
