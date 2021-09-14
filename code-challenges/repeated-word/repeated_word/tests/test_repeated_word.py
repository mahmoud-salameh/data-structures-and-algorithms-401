from repeated_word.repeated_word import *

def test_happy_path():
    string="Once upon a time, there was a brave princess who..."
    
   
    actual=repeated_word(string)
    expected='a' 
    assert actual==expected



def test_edge_case():
    actual=repeated_word()
    expected='the string is empty'
    
    assert actual==expected


def test_expected_failure():
    string = "there was a brave princess who"
    actual=repeated_word(string)
    expected='.' 
    assert actual!=expected