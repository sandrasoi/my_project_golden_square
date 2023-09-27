from lib.diary_entry_final_project import * 
import pytest 


#Diary entry containing #TODO returns True
def test_todo_in_text():
    entry1 = DiaryEntry("Title", "#TODO contents")
    result = entry1.is_todo()
    assert result == True

def test_is_phone_number():
    entry1 = DiaryEntry("Title", "This is 07807377138")
    result = entry1.is_phone_number()
    assert result == "07807377138"