import pytest

from pyswot import is_academic
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
    "expected,email",
    ((True, "alumni.nottingham.ac.uk"), (False, "nottingham.ac.uk"))
)
def test_stoplist(expected,email):
    assert expected == _is_stoplisted(_domain_parts(email))
