# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.running_total_of_content_read = []
        # Side-effects:
        #   Sets the title and contents properties
        

    def count_words(self):
        words = self.contents.split()
        return len(words)


    def reading_time(self, wpm):
        word_list = self.contents.split()
        return len(word_list) / wpm
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        total_words = wpm*minutes
        if len(self.contents.split()) <= total_words:
            return self.contents
        else:
            word_list = self.contents.split()
            result = ' '.join(word_list[len(self.running_total_of_content_read):len(self.running_total_of_content_read)+total_words])
            self.running_total_of_content_read += result.split()
        return result
        

        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass