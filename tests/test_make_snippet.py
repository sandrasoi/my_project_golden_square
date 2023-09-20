from lib.make_snippet import *

def test_make_snippet():
    result = make_snippet("orange apple pear strawberry grapes")
    assert result == "orange apple pear strawberry grapes"


def test_snippet_longer_than_five():
    result = make_snippet("orange apple pear strawberry grapes plum")
    assert result == "orange apple pear strawberry grapes..."