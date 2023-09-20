def reading_time(text):
    split_words_by_space = text.split()
    count_number_of_words = len(split_words_by_space)
    average_reading_time = count_number_of_words/200
    return average_reading_time

print(reading_time("""one two three four five six seven eight nine ten 
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten
one two three four five six seven eight nine ten  
one two three four five six seven eight nine ten  """))

