# App Discovery Parser: AppID Extractor

**Fast, production-friendly parser for extracting Google Play package names and Apple App Store IDs from raw HTML or live URLs.**

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)](#)
[![Coverage](https://img.shields.io/badge/coverage-not%20configured-lightgrey?style=for-the-badge)](#testing)

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Technical Notes](#technical-notes)
  - [Project Structure](#project-structure)
  - [Key Design Decisions](#key-design-decisions)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [Contacts](#contacts)
- [Support the Project](#-support-the-project)

## Features

- **Dual ecosystem parsing in one pass**
  - Extracts Android package names from Google Play links.
  - Extracts numeric App Store IDs from Apple URLs and iTunes-style links.
- **Multi-source input workflow**
  - Add multiple source blocks and parse everything in one run.
  - Supports both **raw HTML paste mode** and **URL fetch mode**.
- **Deterministic deduplication**
  - Removes duplicates while preserving first-seen order, which keeps exports clean without losing practical context.
- **Localization-ready UI**
  - Built-in language support in the app and separate JS locale assets in `locales/`.
- **Operator-centric UX**
  - Quick source switching, expandable source cards, and immediate result metrics.
- **Export-first output**
  - One-click `.txt` downloads for Google Play and App Store IDs (`gp.txt`, `as.txt`).

## Technology Stack

- **Language:** `Python`
- **Framework/UI:** `Streamlit`
- **HTTP Client:** `requests`
- **Parsing strategy:** `re` (Python regular expressions)
- **Frontend styling:** custom CSS (`assets/style.css`)
- **Localization assets:** Python dictionary (`translations.py`) + JS locale modules (`locales/*.js`)

## Technical Notes

### Project Structure

```text
.
├── app.py                # Streamlit entrypoint, UI, input orchestration, result rendering
├── parser_logic.py       # Regex extraction and HTML title detection helpers
├── translations.py       # App localization dictionary used by the Streamlit UI
├── locales/              # Standalone JS locale modules (one file per language)
├── assets/
│   └── style.css         # UI styling layer
├── requirements.txt      # Python dependencies
├── LICENSE               # GPL-3.0 license text
└── README.md             # Project documentation
```

### Key Design Decisions

- **Regex over heavy HTML parsing**
  - The target data follows stable URL-like patterns, so regex is faster, simpler, and easier to maintain for this use case.
- **Stateful multi-source UX with `st.session_state`**
  - Keeps user inputs persistent during UI reruns and enables an efficient “add/remove source” flow.
- **Separated extraction logic**
  - `parser_logic.py` isolates parser behavior from UI code, making it easier to test and evolve safely.
- **Order-preserving deduplication**
  - Uses dictionary-order semantics to preserve the first useful occurrence for analyst workflows.
- **Fail-soft network behavior**
  - URL fetch errors are surfaced in UI without crashing the parsing session.

## Getting Started

### Prerequisites

Make sure your environment has:

- `Python 3.9+` (3.10+ recommended)
- `pip` (latest stable preferred)
- Optional but recommended:
  - `venv` or another virtual environment manager
  - `git`

### Installation

```bash
# 1) Clone the repository
git clone https://github.com/ostinua/app-discovery-parser-appid-extractor.git
cd app-discovery-parser-appid-extractor

# 2) Create and activate a virtual environment
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

# 3) Install dependencies
pip install -r requirements.txt
```

## Testing

There is currently no full automated test suite committed in this repository, but you can still run reliable sanity checks before shipping changes:

```bash
# Dependency integrity check
pip install -r requirements.txt

# Basic parser smoke check
python - <<'PY'
from parser_logic import extract_google_play_ids, extract_app_store_ids
sample = '''
https://play.google.com/store/apps/details?id=com.example.app
https://apps.apple.com/us/app/sample/id123456789
'''
print(extract_google_play_ids(sample))
print(extract_app_store_ids(sample))
PY

# Streamlit app boot check
streamlit run app.py
```

Recommended contributor tooling:

- `pytest` for unit tests
- `ruff`/`flake8` for linting
- `black` for formatting

## Deployment

For production-ish usage, you can deploy this app in a few common ways:

1. **Streamlit Community Cloud**
   - Push to GitHub, configure app entrypoint as `app.py`, and install dependencies from `requirements.txt`.
2. **Container-based deployment**
   - Package the app in Docker and expose the Streamlit port (`8501` by default).
3. **VM/Bare-metal**
   - Run behind a reverse proxy (Nginx/Caddy), pin Python environment, and manage process with `systemd` or `supervisor`.

Minimal local production command:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

## Usage

```bash
# Start the app
streamlit run app.py

# Then open the local URL shown in terminal (usually http://localhost:8501)
```

Typical workflow in the UI:

```text
1) Choose language in the sidebar.
2) Add one or more sources (HTML paste or URL mode).
3) Click "Parse All Data".
4) Review Google Play and App Store panels.
5) Download results as gp.txt / as.txt.
```

Pro tip for data completeness: when scraping store listing pages manually, scroll to the bottom first so lazy-loaded blocks are present in page source.

## Configuration

This project is intentionally low-config and does not require a mandatory `.env` file for baseline execution.

Current runtime knobs are primarily Streamlit flags:

- `--server.address`
- `--server.port`
- `--server.headless`

Example:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501 --server.headless true
```

If you introduce environment variables in future updates, document them here with default values and security notes.

## License

This project is distributed under the **GPL-3.0** license. See [`LICENSE`](LICENSE) for the full legal text.

## Contacts

Maintainer and project author channels:

- Telegram: [@FCTostin](https://t.me/FCTostin)
- YouTube: [FCT-Ostin](https://www.youtube.com/@FCT-Ostin)
- Patreon: [OstinFCT](https://www.patreon.com/OstinFCT)

## ❤️ Support the Project

If you find this tool useful, consider leaving a ⭐ on GitHub or supporting the author directly:

[![Patreon](https://img.shields.io/badge/Patreon-OstinFCT-f96854?style=flat-square&logo=patreon)](https://www.patreon.com/OstinFCT)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-fctostin-29abe0?style=flat-square&logo=ko-fi)](https://ko-fi.com/fctostin)
[![Boosty](https://img.shields.io/badge/Boosty-Support-f15f2c?style=flat-square)](https://boosty.to/ostinfct)
[![YouTube](https://img.shields.io/badge/YouTube-FCT--Ostin-red?style=flat-square&logo=youtube)](https://www.youtube.com/@FCT-Ostin)
[![Telegram](https://img.shields.io/badge/Telegram-FCTostin-2ca5e0?style=flat-square&logo=telegram)](https://t.me/FCTostin)
