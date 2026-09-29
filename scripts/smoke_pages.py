"""Render every page of a Streamlit app and fail if any raises or does not compile.

Piped into `python -` inside the built image by build-image.yml
(SMOKE_PYTHON_SCRIPT). The container health endpoint stays "ok" when a page
throws, so without this a bad image goes Ready and replaces the good pod.

Two things AppTest alone does not catch, both checked here:
  - a page with a SyntaxError or IndentationError: AppTest logs "Script
    compilation error" but reports no exception, so every page is compile()d first
  - a renamed or missing pages/ folder: the glob then finds nothing and the
    run would pass on Home.py alone, so MIN_PAGES must be met

Not caught: a page that calls st.error(...) or st.stop() and otherwise runs.
Runs from the image's WORKDIR, which is where Home.py and pages/ live.
"""
import glob
import os
import sys

from streamlit.testing.v1 import AppTest

# Set to the number of files in pages/ (not counting Home.py). Lower it only when
# a page is removed on purpose.
MIN_PAGES = 3

scripts = ["Home.py"] + sorted(glob.glob("pages/*.py"))
bad = 0

if len(scripts) - 1 < MIN_PAGES:
    print(f"FAIL expected at least {MIN_PAGES} page(s) in pages/, found {len(scripts) - 1}")
    sys.exit(1)

for f in scripts:
    try:
        with open(f, encoding="utf-8") as fh:
            compile(fh.read(), f, "exec")
    except SyntaxError as exc:
        print(f"FAIL {f} does not compile: {exc}")
        bad += 1
        continue
    at = AppTest.from_file(os.path.abspath(f), default_timeout=30).run()
    errors = [str(e.value)[:200] for e in at.exception]
    print(("FAIL " if errors else "ok   ") + f, errors if errors else "")
    bad += bool(errors)

print(f"{len(scripts) - bad} of {len(scripts)} pages rendered")
sys.exit(1 if bad else 0)
