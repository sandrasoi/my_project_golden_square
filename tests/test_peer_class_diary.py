from mocking_bites.peer_class_diary import *
from mocking_bites.peer_class_secret_diary import *
import pytest

def test_return_contents():
    diary = Diary("My contents")
    assert diary.read() == "My contents"