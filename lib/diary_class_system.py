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
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass



