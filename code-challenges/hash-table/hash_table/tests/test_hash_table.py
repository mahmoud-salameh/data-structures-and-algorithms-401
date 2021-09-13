from hash_table.hash_table import *



def test_add():
    test=Hashtable()
    test.add('Mahmoud',555)
    assert test.contains('Mahmoud')==True

def test_get_null():
    test = Hashtable()
    test=test.get('Mahmoud')
    expected=None
    assert test==expected

def test_collision_hashtable():
    test = Hashtable()
    test.add('Mahmoud', 93)
    test.add('nura', 96)
    assert test.get('nura') == 96

def test_collision_retrieve_hashtable():
    test = Hashtable()
    test.add('Mahmoud', 93)
    test.add('nura', 96)
    assert (test.get('nura') == 96 and test.get('Mahmoud')== 93)




