# Next steps for Maurice

1. Open the pull request from `build` to `main` and look at the Netlify deploy preview on your phone and laptop.
2. Generate the 18 hero images listed in docs/image-list.md in Artistly (file name, size and prompt are given).
   Save each under its exact file name in src/static/images/, run `python3 build.py`, commit and push. Until then
   every page shows an existing photo in its place, never a broken image.
3. When you are happy, merge the pull request. Netlify publishes `dist/` from `main`.
4. Optional: add an email address, more social profile URLs (src/data/site.json), and a governing-law line in the
   terms if you want one.
