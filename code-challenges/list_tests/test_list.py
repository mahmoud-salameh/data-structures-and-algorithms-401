
from linked_list.linked_list import (Node, LinkedList, zipLists)



def test_instantiate_empty_linked_list():
    class_input = LinkedList()
    actual = class_input.__str__()
    expected=''
    assert actual == expected


def test_insert():
    class_input = LinkedList()
    class_input.insert("My Name Is Mahmoud")
    actual=class_input.__str__()
    expected='( My Name Is Mahmoud ) -> NULL'
    assert actual == expected

def test_head_value():
    class_input = LinkedList()
    class_input.insert(3)
    actual=class_input.head.value
    expected= 3
    assert actual == expected

def test_insert_multiple_nodes():
    class_input = LinkedList()
    class_input.insertAfter(3, 4)
    class_input.insert(1)
    class_input.insert(2)
    class_input.insert(3)
    actual= class_input.__str__()

    expected='( 3 ) -> ( 2 ) -> ( 1 ) -> NULL'
    assert actual == expected

def test_includes_True():
    class_input = LinkedList()
    class_input.insert(3)
    class_input.insert(2)
    class_input.insert(6)
    class_input.insert(30)
    actual = class_input.includes(2)
    expected = True
    assert actual == expected


def test_return_aclass_input_value():
    class_input =LinkedList()
    class_input.insert(1)
    class_input.insert(2)
    class_input.insert(3)
    class_input.insert(4)
    actual = class_input.__str__()
    expected = '( 4 ) -> ( 3 ) -> ( 2 ) -> ( 1 ) -> NULL'
    assert actual == expected

class_input = LinkedList()
def test_return_aclass_input_values():
    class_input = LinkedList()
    class_input.append(1)
    class_input.append(2)
    class_input.append(3)
    actual = class_input.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> NULL'
    assert actual == expected

def test_add_node_end():
    class_input=LinkedList()
    class_input.insert(1)
    class_input.insert( 2 )
    class_input.append(5)
    actual = class_input.__str__()
    expected='( 2 ) -> ( 1 ) -> ( 5 ) -> NULL'
    assert actual == expected

class_input = LinkedList()

def test_insert_node_before_middle():
    class_input = LinkedList()
    class_input.append(1)
    class_input.append(3)
    class_input.append(4)
    class_input.insertBefore(3, 2)
    actual = class_input.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> NULL'
    assert actual == expected

def test_insert_node_before_head():
    class_input = LinkedList()
    class_input.append(2)
    class_input.append(3)
    class_input.append(4)
    class_input.insertBefore(2, 1)
    actual = class_input.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> NULL'
    assert actual == expected

def test_insert_node_after_middle():
    class_input = LinkedList()
    class_input.append(1)
    class_input.append(2)
    class_input.append(4)
    class_input.insertAfter(2, 3)
    actual = class_input.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> NULL'
    assert actual == expected

def test_insert_node_after_end():
    class_input = LinkedList()
    class_input.append(1)
    class_input.append(2)
    class_input.append(3)
    class_input.insertAfter(3, 4)
    actual = class_input.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> NULL'
    assert actual == expected

def test_k_greater_than_linked_list():
    class_input = LinkedList()
    class_input.append(3)
    class_input.append(2)
    class_input.append(6)
    class_input.append(30)
    actual = class_input.kth_From_End(30)
    expected='Exception'
    assert actual == expected
    
def test_k_same_the_linked_list():
    class_input = LinkedList()
    class_input.append(3)
    class_input.append(2)
    class_input.append(6)
    class_input.append(8)
    actual = class_input.kth_From_End(8)
    expected='Exception'
    assert actual == expected

def test_k_not_postive_intger():
    class_input = LinkedList()
    class_input.append(3)
    class_input.append(2)
    class_input.append(6)
    class_input.append(8)
    actual = class_input.kth_From_End(-21)
    expected="Can't enter a negative number in the input"
    assert actual == expected

def test_k_happy_path():
    class_input = LinkedList()
    class_input.append(3)
    class_input.append(2)
    class_input.append(6)
    class_input.append(8)
    actual = class_input.kth_From_End(3)
    expected = 3
    assert actual == expected

def test_happy_path():
    list_input1 = LinkedList()
    list_input1.append(6)
    list_input1.append(4)
    list_input1.append(2)
    list_input2 = LinkedList()
    list_input2.append(5)
    list_input2.append(3)
    list_input2.append(1)
    actual=zipLists(list_input1, list_input2)
    expected='( 6 ) -> ( 5 ) -> ( 4 ) -> ( 3 ) -> ( 2 ) -> ( 1 ) -> NULL'
    assert actual==expected

def test_edge_case():
    list_input1 = LinkedList()
    list_input1.append(1)
    list_input1.append(6)
    list_input1.append(12)
    list_input2 = LinkedList()
    list_input2.append(3)
    list_input2.append(9)
    actual=zipLists(list_input1, list_input2)
    expected='( 1 ) -> ( 3 ) -> ( 6 ) -> ( 9 ) -> ( 12 ) -> NULL'
    assert actual==expected

