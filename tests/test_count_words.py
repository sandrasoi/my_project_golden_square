from lib.count_words import *

def test_count_words():
    result = count_words("Hello this is a test")
    assert result == 20