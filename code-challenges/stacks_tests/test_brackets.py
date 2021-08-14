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




























# def test_pre_order(prepared_tree):
#     assert prepared_tree.pre_order() == 'ABDECF'


# def test_post_order(prepared_tree):
#     assert prepared_tree.post_order() == 'DEBFCA'

# def test_in_order(prepared_tree):
#     assert prepared_tree.in_order() == 'DBEAFC'


# def test_pre_order_empty_tree():
#     tree = BinaryTree()
#     assert tree.pre_order() == 'The Tree is empty'

# def test_in_order_empty_tree():
#     tree = BinaryTree()
#     assert tree.in_order() == 'The Tree is empty'

# def test_post_order_empty_tree():
#     tree = BinaryTree()
#     assert tree.post_order() == 'The Tree is empty'


# def test_instantiate_an_empty_tree():
#     tree= BinarySearchTree()
#     assert tree.root == None

# def test_instantiate_tree_with_single_root():
#     tree= BinarySearchTree()
#     tree.add(5)
#     assert tree.pre_order() == '5'

# def test_add_left_right_to_tree():
#     tree= BinarySearchTree()
#     tree.add(5)
#     tree.add(4)
#     tree.add(4)
#     tree.add(7)
    
#     assert tree.root.left.value == 4
#     assert tree.root.right.value == 7
#     assert tree.root.left.right.value == 4
#     assert tree.pre_order()=='5447'
#     assert tree.in_order()=='4457'
#     assert tree.post_order()=='4475'



# def test_contains_False():
#     tree= BinarySearchTree()
#     tree.add(5)
#     tree.add(4)
#     tree.add(7)
#     assert tree.contains(8)==False

# def test_contains_True():
#     tree= BinarySearchTree()
#     tree.add(5)
#     tree.add(4)
#     tree.add(7)
#     assert tree.contains(7)==True


# @pytest.fixture
# def prepared_tree():
#     tree = BinaryTree()
#     tree.root = Node('A')
#     tree.root.left = Node('B')
#     tree.root.right = Node('C')
#     tree.root.left.left = Node('D')
#     tree.root.left.right = Node('E')
#     tree.root.right.left = Node('F')
#     return tree