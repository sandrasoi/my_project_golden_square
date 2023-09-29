from mocking_bites.peer_class_diary import *
from mocking_bites.peer_class_secret_diary import *
import pytest

def test_locked_diaries_can_not_be_unlocked():
    diary = Diary("My contents")
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_unlocked_diary_show_contents():
    diary = Diary("My contents")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "My contents"

def test_lock_an_unlocked_diary():
    diary = Diary("My contents")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"