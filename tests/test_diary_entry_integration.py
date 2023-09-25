from lib.diary_entry_class_system import DiaryEntry
from lib.diary_class_system import Diary

""""
Adds two diary entries to Diary and returns all entries
"""
def test_adds_and_lists_diary_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", "contents1")
    diary_entry2 = DiaryEntry("title2", "contents2")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.all()
    assert result == [diary_entry1, diary_entry2]

"""
Adds two diary entries to Diary and counts content of whole diary.
"""
def test_adds_and_counts_all_words_in_diary():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", "One Two")
    diary_entry2 = DiaryEntry("title2", "Three Four Five")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.count_words()
    assert result == 5

def test_count_words_single_entry():
    diary_entry1 = DiaryEntry("title1", "One Two")
    result = diary_entry1.count_words()
    assert result == 2


'''def test_adds_two_entries_reading_time_for_all_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", "One Two")
    diary_entry2 = DiaryEntry("title2", "Three Four Five")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.reading_time(1)
    assert result == 5'''


#Diary doesn't have parameters, has add method that calls instance of diary entry