def is_academic(email: str) -> bool:
    parts = _domain_parts(email)
    return (
        not _is_free(parts)
        and not _is_stoplisted(parts)
        and (_is_under_tld(parts) or bool(_find_school_names(parts)))
    )


def find_school_names(email: str) -> list[str]:
    return _find_school_names(_domain_parts(email))


def is_free(email: str) -> bool:
    parts = _domain_parts(email)

    return _is_free(parts)


def _is_free(parts: list[str]) -> bool:
    from pyswot.vendor.free import FREE

    return _check_set(FREE, parts)


def _is_under_tld(parts: list[str]) -> bool:
    from pyswot.vendor.tlds import TLDS

    return _check_set(TLDS, parts)


def _is_stoplisted(parts: list[str]) -> bool:
    from pyswot.vendor.stoplist import STOPLIST

    return _check_set(STOPLIST, parts)


def _find_school_names(parts: list[str]) -> list[str]:
    from pyswot.vendor.domains import DOMAINS

    key = ""
    for part in parts:
        key = f".{part}{key}"
        try:
            return DOMAINS[key]
        except KeyError:
            continue

    return []


def _domain_parts(email_or_domain: str) -> list[str]:
    email_or_domain = email_or_domain.strip().lower()

    parts = email_or_domain.split("@")[-1].split(".")
    parts.reverse()

    return parts


def _check_set(s: frozenset[str], parts: list[str]) -> bool:
    t = ""
    for part in parts:
        t = f"{part}{t}"
        if t in s:
            return True
        t = f".{t}"
    return False
