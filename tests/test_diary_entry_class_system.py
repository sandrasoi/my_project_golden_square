from lib.diary_entry_class_system import *

def test_reading_time_of_entry():
    diary_entry1 = DiaryEntry("title1", "One Two")
    result = diary_entry1.reading_time(1)
    assert result == 2

def test_reading_chunk_read_in_2_minutes():
    diary_entry2 = DiaryEntry("title2", "Three Four Five")
    result = diary_entry2.reading_chunk(1,2)
    assert result == "Three Four"

def test_reading_chunk_read_in_2_minutes_reminder_after_calling_method_second_time():
    diary_entry2 = DiaryEntry("title2", "Three Four Five")
    diary_entry2.reading_chunk(1,2)
    result = diary_entry2.reading_chunk(1,2)
    assert result == "Five"