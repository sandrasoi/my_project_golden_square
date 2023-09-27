# File: lib/diary.py
#from diary_entry_class_system import DiaryEntry


class Diary:
    def __init__(self):
        self.diary_entries = []
        

    def add(self, entry):
        self.diary_entries.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        

    def all(self):
        #print(self.diary_entries)
        return self.diary_entries
        # Returns:
        #   A list of instances of DiaryEntry
        pass
        

    def count_words(self):
        total_words = 0
        for entry in self.diary_entries:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        total_reading_time = 0
        for entry in self.diary_entries:
            entry_reading_time = entry.reading_time(wpm)
            total_reading_time += entry_reading_time
        return total_reading_time
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        for entry in self.diary_entries:
            if entry.reading_time(wpm) <= minutes:
                return entry
        
        #result = sorted(self.diary_entries, key= [entry.count_words() for entry in self.diary_entries])
        #return result
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        

#sort entries by length



#calculate the number of words that can be read given the parameters
#iterate through entries list and find content that is exactly that length 
#and if not then less

'''
diary = Diary()
diary_entry1 = DiaryEntry("title1", "One Two")
diary_entry2 = DiaryEntry("title2", "Three Four Five")
diary_entry3 = DiaryEntry("title2", "Six Seven Eight Nine")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)
result = diary.find_best_entry_for_reading_time(1,2)
print(result)'''

#new_list = [entry.count_words() for entry in diary.diary_entries]
#print(new_list)

