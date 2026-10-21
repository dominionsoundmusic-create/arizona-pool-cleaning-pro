# QA record (Yuma Playbook 2.0 rebuild, Oct 21 2026)

All results below were produced on the final build (`python3 build.py`, 21 pages) after the fact-check.

## Summary

| Check | Command | Result |
|---|---|---|
| Rules and SEO | `python3 scripts/check.py` | 21 pages, 0 errors, 0 warnings |
| CLAUDE.md final grep (dashes, "we clean", "we repair", "our technicians", "licensed and insured", "background checked", "free estimate", "same-day", "500+", "starting at", Tucson, Phoenix, Scottsdale, Mesa, Gilbert, Pima, Maricopa, San Diego, California, El Centro, Winterhaven, Houston, Texas, (520), (623), (903), 903-636) | `python3 scripts/grep_check.py` | 0 hits in visible text, titles, meta and alt text |
| Old URLs | `python3 scripts/check_old_urls.py --report docs/qa-old-urls.md` | 207 old URLs checked (main's sitemap, every page file on main, old redirect sources, and 88 page files main deleted in Sep 2026, each with and without .html), 0 would 404 |
| Duplication | `python3 scripts/similarity.py --other <tucson>/dist --other <phoenix>/dist --report docs/qa-similarity.md` | see below; no pair above 15%, no shared 8-word run |
| Keyword plan | `python3 scripts/keyword_plan.py` | 122 keywords: 66 assigned, 56 deliberately unused, 0 unclassified |
| Responsive (Chromium, Playwright) | `node scripts/responsive_check.js` | 90 page loads (all 21 pages at 1440, 1024, 768, 390; sample at 1920 and 2560): 0 horizontal overflow, 0 broken images, 0 JS errors, hero edge to edge, hero at most 720px tall with the call button above the fold at 1024+, headline on the left rail at 1440, 1920, 2560 |
| Functional (Chromium) | `node scripts/functional_check.js` | 13 of 13 pass: mobile menu, submenus, Escape, FAQ accordion, one tel number (+19286155224) site-wide, hover menu, skip link, ES toggle cookie, 404, footer links land at top |
| Repeated photos | inline script | no photo appears twice on any page |
| Speed fix | inspection of dist HTML | CSS inlined in `<style>` (no stylesheet link), hero preloaded with WebP srcset 480 to 1920 and fetchpriority high, woff2 preloaded, GA4 loaded on first scroll/click/keydown/touch or 3.5 s after load |

## Duplication (Jaccard on 5-word shingles)

Same-type Yuma pairs: service 21 pairs, max 1.8%; guide 6 pairs, max 1.2%; core pages 10 pairs, max 1.1%;
legal 1 pair, 0.1%; mixed-type pairs max 2.0%. Against Tucson (27 pages): max 1.2%, no shared 8-word run.
Against Phoenix (52 pages): max 1.2%, no shared 8-word run. Range across all comparisons: 0.0% to 2.0%.
Shared template blocks (header, footer, call band, how-it-works strip, disclosure, license note, cards, pills,
sources) are excluded, as in the Tucson build. Full table: docs/qa-similarity.md.

## Route by route (Prompt 16)

Every indexable route has a unique title, a meta description, a canonical on https://yumapoolcleaningpro.com,
Open Graph and Twitter tags with an absolute image, exactly one H1, a single JSON-LD graph (Organization,
WebPage, BreadcrumbList, plus Service, Article or FAQPage as fits) and is in sitemap.xml. /404.html is noindex,
not in the sitemap, and Netlify serves it for unknown paths. Words = all text inside `<main>`.

| Route | Type | Title (chars) | Desc chars | H1 | FAQs | Body images | Words | Result |
|---|---|---|---:|---:|---:|---:|---:|---|
| /404.html | page | Page Not Found \| Yuma Pool Cleaning Pro (39) | 148 | 1 | 0 | 0 | 275 | pass |
| /about/ | about | About Yuma Pool Cleaning Pro: A Free Line, Not a Pool Company (61) | 153 | 1 | 4 | 2 | 1296 | pass |
| /contact/ | contact | Contact Yuma Pool Cleaning Pro: Call the Free Yuma Pool Line (60) | 152 | 1 | 4 | 2 | 999 | pass |
| /faq/ | page | How Often Do You Service a Pool? Yuma Pool FAQ (46) | 150 | 1 | 6 | 2 | 1891 | pass |
| /green-pool-cleanup/ | service | Green Pool Cleaning Services in Yuma, AZ: What a Cleanup Involves (65) | 154 | 1 | 5 | 3 | 2536 | pass |
| /how-it-works/ | page | How the Free Yuma Pool Service Line Works, Step by Step (55) | 169 | 1 | 4 | 2 | 1406 | pass |
| / | page | Pool Service Yuma AZ: One Free Line to a Local Pool Company (59) | 155 | 1 | 5 | 2 | 2358 | pass |
| /is-a-pool-service-worth-it/ | guide | Is a Pool Service Worth It? Deciding in Yuma, Arizona (53) | 166 | 1 | 4 | 3 | 1996 | pass |
| /my-pool-is-green/ | guide | My Pool Is Green, How Do I Fix It? Causes and Safe First Steps (62) | 143 | 1 | 5 | 3 | 2174 | pass |
| /pool-cleaning | service | Pool Cleaning in Yuma: The Tasks, How Often, and Deep Cleans (60) | 156 | 1 | 5 | 3 | 2185 | pass |
| /pool-equipment-repair/ | service | Pool Equipment Repair in Yuma: Filters, Heaters, Salt Cells (59) | 160 | 1 | 5 | 3 | 2841 | pass |
| /pool-maintenance-cost/ | guide | How Much Is Pool Maintenance? Yuma Cost Guide for 2026 (54) | 159 | 1 | 5 | 3 | 2659 | pass |
| /pool-pump-repair/ | service | Pool Pump Repair in Yuma: Symptoms, Costs, Repair or Replace (60) | 150 | 1 | 5 | 2 | 2835 | pass |
| /pool-repair/ | service | Pool Repair in Yuma, AZ: Leaks, Cracks, Lights and Drains (57) | 164 | 1 | 5 | 3 | 2829 | pass |
| /pool-service | service | Pool Maintenance in Yuma, AZ: Weekly Pool Service Plans (55) | 147 | 1 | 5 | 3 | 2365 | pass |
| /pool-tile-cleaning/ | service | Pool Tile Cleaning in Yuma, AZ: Calcium Scale and the White Line (64) | 148 | 1 | 5 | 3 | 2586 | pass |
| /privacy-policy.html | legal | Privacy Policy \| Yuma Pool Cleaning Pro (39) | 151 | 1 | 0 | 0 | 690 | pass |
| /service-areas/ | page | Pool Service Yuma Foothills, Somerton, San Luis and Wellton (59) | 144 | 1 | 5 | 3 | 2188 | pass |
| /services/ | page | Yuma Pool Services: Care, Repairs and Problem Water (51) | 157 | 1 | 4 | 2 | 2320 | pass |
| /terms.html | legal | Terms of Use \| Yuma Pool Cleaning Pro (37) | 155 | 1 | 0 | 0 | 776 | pass |
| /yuma-pool-maintenance-schedule/ | guide | Pool Maintenance Schedule for Yuma: Weekly, Monthly, Seasonal (61) | 162 | 1 | 5 | 3 | 2847 | pass |

## Not verified here

- Netlify behavior (redirects, 404 status, pretty URLs) on the deploy preview: checked by script against the
  _redirects rules and file layout, not on Netlify itself. Check the PR's deploy preview.
- Google Analytics and Google Translate requests: the sandbox cannot reach Google, so tag loading and the actual
  Spanish translation were not observed (the cookie and loader logic were).
- Phone call flow (automated assistant, transfer): not tested; it is outside the website.
- Fact-check method limit: sources were verified through search summaries, not opened (docs/fact-check.md).
