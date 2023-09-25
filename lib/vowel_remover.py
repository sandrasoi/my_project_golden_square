# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]
        self.new_phrase = ""

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() not in self.vowels:
                self.new_phrase += self.text[i]
                #self.text = self.text[:i] + self.text[i+1:]
            i += 1
        return self.new_phrase

remover = VowelRemover("This is a sentence")
result = remover.remove_vowels()
print(result)