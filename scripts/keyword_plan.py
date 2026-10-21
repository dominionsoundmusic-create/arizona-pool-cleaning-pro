#!/usr/bin/env python3
"""Assign every keyword in keywords/Yuma-Pool-Keywords.xlsx to a page (target or supporting)
or to the deliberately-unused list with a one-line reason. Writes docs/keyword-plan.md.

Usage: python3 scripts/keyword_plan.py   (exit code 1 if any row is left unclassified)
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "home": "/", "services": "/services/", "areas": "/service-areas/", "faq": "/faq/",
    "service": "/pool-service", "cleaning": "/pool-cleaning", "repair": "/pool-repair/",
    "pump": "/pool-pump-repair/", "equipment": "/pool-equipment-repair/", "green": "/green-pool-cleanup/",
    "tile": "/pool-tile-cleaning/",
    "g-cost": "/pool-maintenance-cost/", "g-schedule": "/yuma-pool-maintenance-schedule/",
    "g-green": "/my-pool-is-green/", "g-worth": "/is-a-pool-service-worth-it/",
}

# Primary target keyword(s) of each page. The rest of its assigned keywords are supporting.
TARGETS = {
    "pool service yuma az": "home", "yuma pool service": "home", "pool service yuma": "home",
    "yuma pool services": "services",
    "pool service yuma foothills": "areas",
    "how often do you service a pool": "faq",
    "pool maintenance yuma az": "service", "pool maintenance yuma": "service",
    "pool cleaning yuma": "cleaning",
    "pool repair yuma": "repair", "yuma pool repair": "repair",
    "pool pump repair yuma": "pump",
    "pool equipment repair yuma": "equipment",
    "green pool cleaning yuma": "green", "green pool cleaning services": "green",
    "pool tile cleaning az": "tile", "pool tile cleaning yuma": "tile",
    "how much is pool maintenance": "g-cost",
    "pool maintenance schedule": "g-schedule",
    "my pool is green how do i fix it": "g-green",
    "is a pool service worth it": "g-worth",
}

U_PUBLIC = "a public pool, city pool or pool-hours search (CLAUDE.md: public-pool searches go in the unused list)"
U_BRAND = "names a specific pool company (CLAUDE.md rule 3: never name a pool company)"
U_REVIEWS = "a search for reviews; the site has no reviews and never invents them (CLAUDE.md rule 2)"
U_PLACE = "a place outside Yuma County, Arizona, or another place named San Luis (CLAUDE.md rule 4)"
U_JOBS = "jobs for pool workers, not a homeowner service"
U_OFF = "off-topic: not about caring for or repairing a home pool"
U_HEAD = ("ambiguous head term: the file pairs it with public-pool rows (\"yuma pool hours\"), and the City of Yuma runs "
          "public pools, so the intent is mostly a city pool, not pool service")

UNUSED = [  # first match wins
    (r"\bjobs?\b", U_JOBS),
    (r"reviews", U_REVIEWS),
    (r"tile shower|wellton az power", U_OFF),
    (r"yuma pro pool|crystal clear|jac pool|green valley pool service|wells pool service", U_BRAND),
    (r"san diego|gilbert|queen creek|san tan|san bernardino|san juan capistrano|la mesa|san rafael|la quinta|sun city|"
     r"kingman|san ramon|los altos|san luis obispo|wickenburg|\b85\d{3}\b|tolleson|san jacinto|san pedro|san carlos|"
     r"mineral wells|tucson|el paso|phoenix", U_PLACE),
    (r"hours|^wellton pool$|^wellton az pool$|^somerton az pool$|^san luis arizona pool$", U_PUBLIC),
    (r"^yuma pool$|^pool yuma$", U_HEAD),
]

EXPLICIT = {  # supporting keywords, by page
    "home": ["pool service in yuma", "best pool service yuma az"],
    "areas": ["pool service somerton az", "pool service san luis az", "pool service wellton az"],
    "faq": ["how often should you service your pool", "how often to service a pool", "how often is pool service"],
    "service": ["what does pool maintenance include"],
    "cleaning": ["pool cleaning service yuma az", "pool cleaning services yuma az", "pool cleaners in yuma az",
                 "how often pool cleaning", "how many times should a pool be cleaned", "how often do you clean your pool",
                 "how often to clean your pool", "how often do you get your pool cleaned",
                 "how often should you clean your pool skimmer", "how often pool cleaner"],
    "repair": ["underwater pool repair near me"],
    "pump": ["how often do pool pumps need to be replaced", "how often do you replace a pool pump",
             "how often does your pool pump need to run"],
    "equipment": ["how often should pool equipment be serviced", "how often does pool equipment need to be replaced"],
    "green": ["how much does it cost to fix a green pool"],
    "tile": ["how often should you clean pool tile", "how often to clean pool tile"],
    "g-cost": ["how much is a pool service per month", "how much is a pool maintenance service", "pool maintenance per month",
               "pool maintenance fees", "pool service per month", "how much does it cost to get my pool cleaned",
               "pool service quote", "pool cleaning quotes", "how much is pool service in az"],
    "g-schedule": ["how often pool maintenance", "pool maintenance tips and tricks", "pool water maintenance guide",
                   "how often should you maintenance your pool", "how often is pool maintenance required",
                   "how often should you clean your pool in the winter"],
    "g-green": ["what is the fastest way to clean a green pool", "why is my pool green after cleaning"],
}
SUPPORT = {kw: page for page, kws in EXPLICIT.items() for kw in kws}


def classify(kw):
    k = kw.lower().strip()
    if k in TARGETS:
        return ("page", TARGETS[k])
    if k in SUPPORT:
        return ("page", SUPPORT[k])
    for pat, why in UNUSED:
        if re.search(pat, k):
            return ("unused", why)
    return None


def main():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "Yuma-Pool-Keywords.xlsx", read_only=True)
    rows = list(wb["ALL"].iter_rows(values_only=True))[1:]
    types = {}
    for ws in wb.worksheets[1:]:
        for r in list(ws.iter_rows(values_only=True))[1:]:
            if r[0]:
                types[r[0]] = r[1]
    seen, assigned, unused, missing = set(), defaultdict(list), [], []
    for kw, vol, sd, cpc, seeds in rows:
        if not kw or kw in seen:
            continue
        seen.add(kw)
        typ = types.get(kw, "")
        c = classify(kw)
        if c is None:
            missing.append(kw)
            continue
        kind, val = c
        if kind == "unused":
            unused.append((kw, vol, sd, typ, val))
            continue
        url = PAGES[val]
        role = "TARGET" if kw.lower() in TARGETS else "supporting"
        if role == "supporting" and re.search(r"near me\b", kw):
            role = "supporting (near me: national volume)"
        elif role == "supporting" and not re.search(r"yuma|arizona|\baz\b|somerton|san luis|wellton|foothills", kw):
            role = "supporting (national volume)"
        assigned[url].append((kw, vol, sd, typ, role))
    if missing:
        print("UNCLASSIFIED:", missing)
        return 1
    n_as = sum(len(v) for v in assigned.values())
    out = ["# Keyword plan (Yuma Pool Cleaning Pro, Oct 21 2026)", "",
           "Source: keywords/Yuma-Pool-Keywords.xlsx (Ubersuggest, United States, pulled Oct 20 2026), ALL tab,",
           f"{len(seen)} unique keywords. Generated by `python3 scripts/keyword_plan.py`; every keyword is either assigned to",
           "one page (as its TARGET or a supporting keyword) or listed as deliberately unused with a reason.", "",
           "Rules applied:",
           "- \"Near me\" terms and terms with no place name (\"how much is pool maintenance\" 720, \"pool maintenance",
           "  schedule\" 480) carry national volume. They are supporting keywords or guide targets only, never read as",
           "  proof of Yuma demand. Each guide answers its national question for a Yuma reader.",
           "- Town pages: Maurice's rule is that any town with 10 or more searches a month for a POOL SERVICE keyword gets",
           "  its own page. No town qualifies: Fortuna Foothills (\"pool service yuma foothills\" 0), Somerton (\"pool",
           "  service somerton az\" 0; \"somerton pool hours\" 20 and \"somerton az pool\" 10 are public-pool searches),",
           "  San Luis (\"pool service san luis az\" 0, \"san luis arizona pool\" 0; the other San Luis rows are other",
           "  places), Wellton (\"pool service wellton az\" 0; \"wellton pool\" 30 and \"wellton az pool\" 10 are",
           "  public-pool searches) and Gadsden (no rows). So no town pages: the towns are covered honestly on",
           "  /service-areas/.",
           "- Public-pool searches, company names, review searches, jobs and places outside Yuma County are unused.",
           "- Volume / SD = monthly searches / Ubersuggest SEO difficulty. Type is the row type in the seed tabs.", "",
           f"Assigned: {n_as}. Unused: {len(unused)}.", "", "## Assigned keywords by page", ""]
    for url in PAGES.values():
        if url not in assigned:
            continue
        out += [f"### {url}", "", "| Keyword | Volume | SD | Type | Role |", "|---|---:|---:|---|---|"]
        for kw, vol, sd, typ, role in sorted(assigned[url], key=lambda r: (r[4] != "TARGET", -(r[1] or 0), r[0])):
            out.append(f"| {kw} | {vol:,} | {sd} | {typ} | {role} |")
        out.append("")
    out += ["## Deliberately unused", "", "| Keyword | Volume | SD | Type | Reason |", "|---|---:|---:|---|---|"]
    for kw, vol, sd, typ, why in sorted(unused, key=lambda r: (r[4], -(r[1] or 0), r[0])):
        out.append(f"| {kw} | {vol:,} | {sd} | {typ} | {why} |")
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(out) + "\n")
    for url in PAGES.values():
        if url in assigned:
            t = [r[0] for r in assigned[url] if r[4] == "TARGET"]
            print(f"{url:40s} {len(assigned[url]):3d} kws  target={', '.join(t) or 'NONE'}")
    print(f"assigned {n_as}, unused {len(unused)}, total {len(seen)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
