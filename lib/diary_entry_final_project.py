class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def reading_time(self,wpm):
        word_list = self.contents.split()
        return len(word_list) / wpm
    
    def is_todo(self):
        if "#TODO" in self.contents:
            return True
        
    def is_phone_number(self):
        split_words = self.contents.split()
        for word in split_words:
            if len(word) == 11 and word[0] == "0":
                return word