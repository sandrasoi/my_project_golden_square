from lib.reading_time import *

def test_reading_time_200_words():
    result = reading_time("""one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten  
        "one two three four five six seven eight nine ten  
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten  
        "one two three four five six seven eight nine ten   
        "one two three four five six seven eight nine ten                                                                                       
        """)
    
    assert result == 1

def test_reading_time_100_words():
    result = reading_time("""one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten
        "one two three four five six seven eight nine ten  
        "one two three four five six seven eight nine ten                                                                                         
        """)
    
    assert result == 0.5