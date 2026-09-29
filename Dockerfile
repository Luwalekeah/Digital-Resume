# Streamlit app image. Used by Digital-Resume; tested there in a real browser.
#
# Python 3.11 is the minor the app was tested on. Bump it deliberately, together
# with a browser check of every page.
#
# Runs as uid 10001 with a read-only root filesystem: nothing is written under
# /app, HOME points at /tmp (an emptyDir in the pod), and bytecode is not
# written. Streamlit reads project config from ./.streamlit/config.toml in the
# working directory (and a per-user file under HOME, which is empty here). This
# repo keeps its theme at static/.streamlit/config.toml, which is never read, so
# the app runs on Streamlit's default theme (checked in a browser). The README's Render start command runs it from the repo root the same
# way, so the migration keeps the look unchanged (the live service's real start
# command is unconfirmed). Moving the file to .streamlit/ is a visual change and a
# separate decision.
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    HOME=/tmp

WORKDIR /app

# Dependencies first so the layer caches until requirements.txt changes.
COPY requirements.txt .
RUN pip install -r requirements.txt

# What the image must not carry (.git, an abandoned sibling project) is listed in
# .dockerignore, next to this file.
COPY . .

USER 10001:10001
EXPOSE 8501

# --server.address 0.0.0.0: reachable from the pod network, not just loopback.
# --server.headless: no browser, no first-run email prompt (which would block).
CMD ["streamlit", "run", "Home.py", \
     "--server.port=8501", "--server.address=0.0.0.0", \
     "--server.headless=true", "--browser.gatherUsageStats=false"]
