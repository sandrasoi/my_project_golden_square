def make_snippet(string):
    #split string by word
    split_words_by_space = string.split()
    if len(split_words_by_space) <6:
        #if number of words is less than 6, return string
        return string
    else:
        #else show the first 5 words
        first_five_words = split_words_by_space[0:5]
        return ' '.join(str(word) for word in first_five_words) + "..."

print(make_snippet("orange apple pear strawberry grapes plum"))
print("orange")

