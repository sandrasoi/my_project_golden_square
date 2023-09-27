from lib.diary_entry_final_project import*
from lib.diary_final_project import*

def test_diary_entries_list():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "Contents1")
    diary_entry2 = DiaryEntry("Title2", "Contents2")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.diary_entries
    assert result == [diary_entry1, diary_entry2]

def test_best_entry_to_read_given_wpm1_time_2():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", "One Two")
    diary_entry2 = DiaryEntry("title2", "Three Four Five")
    diary_entry3 = DiaryEntry("title2", "Six Seven Eight Nine")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.find_best_entry_for_reading_time(1,2)
    assert result == diary_entry1

def test_best_entry_to_read_given_wpm1_time_2():
    diary = Diary()
    diary_entry0 = DiaryEntry("title0", 'One')
    diary_entry1 = DiaryEntry("title1", "One Two")
    diary_entry2 = DiaryEntry("title2", "Three Four Five")
    diary_entry3 = DiaryEntry("title2", "Six Seven Eight Nine")
    diary.add(diary_entry0)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.find_best_entry_for_reading_time(1,2)
    assert result == [diary_entry0, diary_entry1]

def test_list_of_todos(): 
    diary = Diary()
    diary_entry0 = DiaryEntry("title0", '07802000000')
    diary_entry1 = DiaryEntry("title1", "#TODO One Two")
    diary_entry2 = DiaryEntry("title2", "07802123456")
    diary_entry3 = DiaryEntry("title2", "#TODO Six Seven Eight Nine")
    diary.add(diary_entry0)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.todo_list()
    assert result == ["#TODO One Two", "#TODO Six Seven Eight Nine"]

def test_phone_number_list():
    diary = Diary()
    diary_entry0 = DiaryEntry("title0", 'words words words 07802000000')
    diary_entry1 = DiaryEntry("title1", "One Two")
    diary_entry2 = DiaryEntry("title2", "07802123456")
    diary_entry3 = DiaryEntry("title2", "Six Seven Eight Nine")
    diary.add(diary_entry0)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.phone_number_list()
    assert result == ["07802000000", "07802123456"]
