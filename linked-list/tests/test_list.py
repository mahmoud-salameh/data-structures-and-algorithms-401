from linked_list import __version__
from linked_list.linked_list import (Node, LinkedList,)

def test_instantiate_empty_linked_list():
    class_input = LinkedList()
    actual = class_input.__str__()
    expected=''
    assert actual==expected

def test_insert():
    class_input = LinkedList()
    class_input.insert("My Name Is Mahmoud")
    actual=class_input.__str__()
    expected='( My Name Is Mahmoud ) -> NULL'
    assert actual==expected

def test_head_value():
    class_input = LinkedList()
    class_input.insert(3)
    actual=class_input.head.value
    expected= 3
    assert actual==expected

def test_insert_multiple_nodes():
    class_input = LinkedList()
    class_input.insert(1)
    class_input.insert(2)
    class_input.insert(3)
    actual= class_input.__str__()

    expected='( 3 ) -> ( 2 ) -> ( 1 ) -> NULL'
    assert actual==expected

def test_includes_True():
    class_input = LinkedList()
    class_input.insert(3)
    class_input.insert(2)
    class_input.insert(6)
    class_input.insert(30)
    actual = class_input.includes(2)
    expected = True
    assert actual == expected

def test_includes_False():
    class_input = LinkedList()
    class_input.insert(3)
    class_input.insert(2)
    class_input.insert(6)
    class_input.insert(30)
    actual = class_input.includes(110)
    expected = False
    assert actual == expected

def test_return_all_value():
    class_input =LinkedList()
    class_input.insert(1)
    class_input.insert(2)
    class_input.insert(3)
    class_input.insert(4)
    actual = class_input.__str__()
    expected = '( 4 ) -> ( 3 ) -> ( 2 ) -> ( 1 ) -> NULL'
    assert actual == expected