#from diary_entry_final_project import*
class Diary():
    def __init__(self):
        self.diary_entries = []

    def add(self, entry):
        self.diary_entries.append(entry)

    def diary_entries(self):
        return self.diary_entries
    
    def find_best_entry_for_reading_time(self,wpm, minutes):
        diary_entries_that_can_be_read = []
        for entry in self.diary_entries:
            if entry.reading_time(wpm) <= minutes:
                diary_entries_that_can_be_read.append(entry)
        return diary_entries_that_can_be_read
    
    def todo_list(self):
        diary_entries_with_todos= []
        for entry in self.diary_entries:
            if entry.is_todo():
                diary_entries_with_todos.append(entry.contents)
        return diary_entries_with_todos

    def phone_number_list(self):
        diary_entries_with_number = []
        for entry in self.diary_entries:
            number = entry.is_phone_number()
            if number != None:
                diary_entries_with_number.append(number)
        return diary_entries_with_number
