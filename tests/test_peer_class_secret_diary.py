from mocking_bites.peer_class_secret_diary import *
from unittest.mock import Mock
import pytest

def test_initially_locked_so_cant_read():
    fakediary = Mock()
    secret_diary = SecretDiary(fakediary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_unlocked_diary_show_contents():
    fakediary = Mock()
    fakediary.read.return_value = "My contents"
    secret_diary = SecretDiary(fakediary)
    secret_diary.unlock()
    assert secret_diary.read() == "My contents"

def test_lock_an_unlocked_diary():
    fakediary = Mock()
    secret_diary = SecretDiary(fakediary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"




