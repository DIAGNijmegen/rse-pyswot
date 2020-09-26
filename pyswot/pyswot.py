from pathlib import Path
from typing import FrozenSet, List


def _read_list(rel_path: str):
    with open(Path(__file__).parent / rel_path, "r") as f:
        stoplist = frozenset(f.read().splitlines())
    return stoplist


STOPLIST = _read_list("swot/lib/domains/stoplist.txt")
TLDS = _read_list("swot/lib/domains/tlds.txt")


def is_academic(email: str) -> bool:
    parts = _domain_parts(email)
    return not _is_stoplisted(parts) and (
        _is_under_tld(parts) or bool(_find_school_names(parts))
    )


def find_school_names(email: str) -> List[str]:
    return _find_school_names(_domain_parts(email))


def _is_under_tld(parts: List[str]) -> bool:
    return _check_set(TLDS, parts)


def _is_stoplisted(parts: List[str]) -> bool:
    return _check_set(STOPLIST, parts)


def _find_school_names(parts: List[str]) -> List[str]:
    resource_path = Path("swot/lib/domains/")

    for part in parts:
        resource_path /= part
        try:
            school = _read_list(f"{resource_path}.txt")
            return list(school)
        except FileNotFoundError:
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
