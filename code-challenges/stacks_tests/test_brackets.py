from stack_and_queue.stack_queue_brackets import *
import pytest

def test_happypath():
    assert the_paran_balanced('{}') == True
    assert the_paran_balanced('{}(){}') == True
    assert the_paran_balanced('(){}[[]]') == True


def test_Expected_failure():
    assert the_paran_balanced('[({}]') != True


def test_Edge_Case():
    assert the_paran_balanced('(](') == False
    assert the_paran_balanced('{(})') == False
    assert the_paran_balanced('{') == False
    assert the_paran_balanced(')') == False
    assert the_paran_balanced('[}') == False