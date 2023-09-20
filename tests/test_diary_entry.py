from lib.diary_entry import *

#check format returned is correct
def test_format_diary():
    diary_entry = DiaryEntry("Wednesday 20 September", "This is my first entry")
    assert diary_entry.format() == "Wednesday 20 September: This is my first entry"