import pytest

from pyswot import is_academic, find_school_names
from pyswot.pyswot import _domain_parts, _is_stoplisted


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
        (True, "lee@mother.edu.ru"),
        (True, "lee@ucy.ac.cy"),
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
        (True, "mother.edu.ru"),
        (True, "ucy.ac.cy"),
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
        # Iran sanctions are lifted
        (True, "lee@acmt.ac.ir"),
    ),
)
def test_swot(expected, email):
    assert expected == is_academic(email)


@pytest.mark.parametrize(
    "expected,email", ((True, "alumni.nottingham.ac.uk"), (False, "nottingham.ac.uk"))
)
def test_stoplist(expected, email):
    assert expected == _is_stoplisted(_domain_parts(email))


def test_find_school_names():
    assert "University of Strathclyde" in find_school_names("lreilly@cs.strath.ac.uk")
    assert "uka tarsadia university,bardoli" in find_school_names(
        "lreilly@cs.strath.ac.uk"
    )
    assert ["BRG Fadingerstraße Linz, Austria"] == find_school_names("lreilly@fadi.at")
    assert ["St. Petersburg State University"] == find_school_names("max@spbu.ru ")
    assert len(find_school_names("foo@shop.com")) == 0
