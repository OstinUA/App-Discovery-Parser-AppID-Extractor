import re

# Pre-compile all patterns once at module load.
# Eliminates per-call regex compilation (O(P) overhead per call, where P = pattern length).
_GP_PATTERN = re.compile(r'/store/apps/details\?id=([a-zA-Z0-9._]+)')

# Single combined App Store pattern replaces two separate patterns, halving HTML scan passes.
# On each match exactly one group is non-empty: g1 for path-form, g2 for domain-form.
_AS_PATTERN = re.compile(
    r'/app/[^"\'\s<>]*/id(\d{6,})'
    r'|(?:apps\.apple\.com|itunes\.apple\.com)[^"\'\s<>]*\bid(\d{6,})'
)

_TITLE_PATTERN = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)


def extract_google_play_ids(html_content: str) -> list[str]:
    return list(dict.fromkeys(_GP_PATTERN.findall(html_content)))


def extract_app_store_ids(html_content: str) -> list[str]:
    # findall returns [(g1, g2), ...]; exactly one group is non-empty per match
    ids = [g1 or g2 for g1, g2 in _AS_PATTERN.findall(html_content)]
    return list(dict.fromkeys(ids))


def extract_all_ids(html_content: str) -> tuple[list[str], list[str]]:
    """Return (google_play_ids, app_store_ids) in one call to avoid redundant string passing."""
    return extract_google_play_ids(html_content), extract_app_store_ids(html_content)


def get_page_title(html_content: str) -> str | None:
    m = _TITLE_PATTERN.search(html_content)
    return m.group(1).strip() if m else None
