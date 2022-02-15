import os
from pathlib import Path

import pytest

from pyswot import find_school_names, is_academic
from pyswot.pyswot import _domain_parts, _find_school_names, _is_stoplisted


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
        (True, "lee@xmu.edu.my"),
        (True, "lee@uha.fr"),
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
    assert ["BRG Fadingerstraße Linz, Austria"] == find_school_names("lrei@fadi.at")
    assert "St. Petersburg State University" in find_school_names("max@spbu.ru ")
    assert len(find_school_names("foo@shop.com")) == 0


def test_non_utf8_source():
    assert find_school_names("myself@cirvianum.cat") == [None]
    assert is_academic("myself@cirvianum.cat")


def test_files_are_utf8(monkeypatch):
    rootdir = Path(__file__).parent.parent / "pyswot" / "swot" / "lib" / "domains"

    non_unicode_files = []

    for subdir, _, files in os.walk(rootdir):
        for file in files:
            rel_file = str(os.path.relpath(os.path.join(subdir, file), rootdir))
            domain_parts = rel_file.split(".txt")[0].split(os.path.sep)
            try:
                _find_school_names(domain_parts)
            except UnicodeDecodeError:
                non_unicode_files.append(rel_file)

    assert non_unicode_files == []
