class GrammarStats:
    def __init__(self):
        self.running_total_of_text_passed = 0
        self.running_total_of_text_not_passed = 0

    def check(self, text):
        end_sentence_symbols = [".", "!", "?"]
        if text[0].isupper() and any(char in end_sentence_symbols for char in text[-1]):
            print(any(char in end_sentence_symbols for char in text[-1]))
            self.running_total_of_text_passed +=1
            return True
        else:
            self.running_total_of_text_not_passed +=1
            return False
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        pass

    def percentage_good(self):
        return self.running_total_of_text_passed/(self.running_total_of_text_passed+self.running_total_of_text_not_passed)*100
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        

grammarstats = GrammarStats()
result = grammarstats.check("This is a good sentence")
print(result)

