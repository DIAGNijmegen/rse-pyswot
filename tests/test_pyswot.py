import pytest

from pyswot import find_school_names, is_academic
from pyswot.pyswot import _domain_parts, _is_stoplisted, is_free


@pytest.mark.parametrize(
    "expected,email",
    (
        (True, "lreilly@stanford.edu"),
        (True, "LREILLY@STANFORD.EDU"),
        (True, "Lreilly@Stanford.Edu"),
        (True, "lreilly@slac.stanford.edu"),
        (True, "lreilly@strath.ac.uk"),
        (True, "lreilly@soft-eng.strath.ac.uk"),
        (True, "lee@ugr.es"),
        (True, "lee@uottawa.ca"),
        (True, "lee@ucy.ac.cy"),
        (False, "lee@mother.edu.ru"),
        (False, "lee@leerilly.net"),
        (False, "lee@gmail.com"),
        (False, "lee@stanford.edu.com"),
        (False, "lee@strath.ac.uk.com"),
        (True, "stanford.edu"),
        (True, "slac.stanford.edu"),
        (True, "www.stanford.edu"),
        (True, "http://www.stanford.edu"),
        # Not handling this
        # (True, "http://www.stanford.edu:9393"),
        (True, "strath.ac.uk"),
        (True, "soft-eng.strath.ac.uk"),
        (True, "ugr.es"),
        (True, "uottawa.ca"),
        (True, "ucy.ac.cy"),
        (False, "mother.edu.ru"),
        (False, "leerilly.net"),
        (False, "gmail.com"),
        (False, "stanford.edu.com"),
        (False, "strath.ac.uk.com"),
        (False, ""),
        (False, "the"),
        (True, " stanford.edu"),
        (True, "lee@strath.ac.uk "),
        (False, " gmail.com "),
        (True, "lee@stud.uni-corvinus.hu"),
        (True, "lee@harvard.edu"),
        (True, "lee@mail.harvard.edu"),
        (False, "imposter@si.edu"),
        (False, "lee@mdu.edu.rs"),
        (False, "lee@temporam.com"),
        (False, "lee@mona.edu.kg"),
        (False, "lee@mona.edu.pl"),
        (False, "lee@zl.edu.kg"),
        (False, "lee@lw.edu.kg"),
        (False, "lee@edumail.edu.pl"),
        # Iran sanctions are lifted
        (True, "lee@acmt.ac.ir"),
        (True, "lee@xmu.edu.my"),
        (True, "lee@uha.fr"),
    ),
)
def test_swot(expected: bool, email: str) -> None:
    assert expected == is_academic(email)


@pytest.mark.parametrize(
    "expected,email",
    ((True, "alumni.nottingham.ac.uk"), (False, "nottingham.ac.uk")),
)
def test_stoplist(expected: bool, email: str) -> None:
    assert expected == _is_stoplisted(_domain_parts(email))


def test_find_school_names() -> None:
    assert "University of Strathclyde" in find_school_names(
        "lreilly@cs.strath.ac.uk"
    )
    assert "uka tarsadia university,bardoli" in find_school_names(
        "lreilly@cs.strath.ac.uk"
    )
    assert ["BRG Fadingerstraße Linz, Austria"] == find_school_names(
        "lrei@fadi.at"
    )
    assert "St. Petersburg State University" in find_school_names(
        "max@spbu.ru "
    )
    assert len(find_school_names("foo@shop.com")) == 0


def test_non_utf8_source() -> None:
    assert find_school_names("myself@cirvianum.cat") == [
        "Institut Cirviànum de Torelló"
    ]
    assert is_academic("myself@cirvianum.cat")


@pytest.mark.parametrize(
    "expected,email",
    (
        (True, "lreilly@proton.me"),
        (True, "LREILLY@PROTON.ME"),
        (True, "lreilly@yahoo.com"),
        (False, "lreilly@google.com"),
    ),
)
def test_is_free(expected: bool, email: str) -> None:
    assert is_free(email) == expected
