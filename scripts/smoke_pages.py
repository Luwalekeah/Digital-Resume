"""Render every page of a Streamlit app and fail if any raises.

Piped into `python -` inside the built image by build-image.yml
(SMOKE_PYTHON_SCRIPT). The container health endpoint stays "ok" when a page
throws, so without this a bad image goes Ready and replaces the good pod.

Runs from the image's WORKDIR, which is where Home.py and pages/ live.
"""
import glob
import os
import sys

from streamlit.testing.v1 import AppTest

scripts = ["Home.py"] + sorted(glob.glob("pages/*.py"))
bad = 0
for f in scripts:
    at = AppTest.from_file(os.path.abspath(f), default_timeout=30).run()
    errors = [str(e.value)[:200] for e in at.exception]
    print(("FAIL " if errors else "ok   ") + f, errors if errors else "")
    bad += bool(errors)
print(f"{len(scripts) - bad} of {len(scripts)} pages rendered")
sys.exit(1 if bad else 0)
