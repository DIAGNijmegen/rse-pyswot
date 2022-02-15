from pathlib import Path
from typing import FrozenSet, List, Optional

from pyswot.vendor.domains import DOMAINS
from pyswot.vendor.stoplist import STOPLIST
from pyswot.vendor.tlds import TLDS


def _read_list(rel_path: str):
    with open(Path(__file__).parent / rel_path) as f:
        stoplist = frozenset(f.read().splitlines())
    return stoplist


def is_academic(email: str) -> bool:
    parts = _domain_parts(email)
    return not _is_stoplisted(parts) and (
        _is_under_tld(parts) or bool(_find_school_names(parts))
    )


def find_school_names(email: str) -> List[Optional[str]]:
    return _find_school_names(_domain_parts(email))


def _is_under_tld(parts: List[str]) -> bool:
    return _check_set(TLDS, parts)


def _is_stoplisted(parts: List[str]) -> bool:
    return _check_set(STOPLIST, parts)


def _find_school_names(parts: List[str]) -> List[Optional[str]]:
    key = ""
    for part in parts:
        key = f".{part}{key}"
        try:
            return DOMAINS[key]
        except KeyError:
            continue

    return []


def _domain_parts(email_or_domain: str) -> List[str]:
    email_or_domain = email_or_domain.strip().lower()

    parts = email_or_domain.split("@")[-1].split(".")
    parts.reverse()

    return parts


def _check_set(s: FrozenSet[str], parts: List[str]) -> bool:
    t = ""
    for part in parts:
        t = f"{part}{t}"
        if t in s:
            return True
        t = f".{t}"
    return False
