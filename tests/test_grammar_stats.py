from lib.grammar_stats import *

def test_correct_grammar():
    grammarstats = GrammarStats()
    result = grammarstats.check("This is a good sentence.")
    assert result == True

def test_percentage_text_passing_check_one_sentence():
    grammarstats = GrammarStats()
    grammarstats.check("This is a good sentence.")
    result = grammarstats.percentage_good()
    assert result == 100