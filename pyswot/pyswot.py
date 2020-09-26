from pathlib import Path
from typing import FrozenSet, List


def _get_stoplist():
    with open(Path(__file__).parent / "swot/lib/domains/stoplist.txt", "r") as f:
        stoplist = frozenset(f.read().splitlines())
    return stoplist

STOPLIST = _get_stoplist()

def is_academic(email: str) -> bool:
    parts = _domain_parts(email)
    return not _is_stoplisted(parts)

def _domain_parts(email_or_domain: str) -> List[str]:
    email_or_domain = email_or_domain.strip().lower()

    parts = email_or_domain.split("@")[-1].split(".")
    parts.reverse()

    return parts

def _is_stoplisted(parts: List[str]) -> bool:
    return _check_set(STOPLIST, parts)

def _check_set(s: FrozenSet[str], parts: List[str]) -> bool:
    t = ""
    for part in parts:
        t = f"{part}{t}"
        if t in s:
            return True
        t = f".{t}"
    return False
