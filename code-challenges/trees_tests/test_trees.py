from trees.binary_tree import *
import pytest


def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order_print() == 'ABDECF'


def test_post_order(prepared_tree):
    assert prepared_tree.post_order_print() == 'DEBFCA'

def test_in_order(prepared_tree):
    assert prepared_tree.in_order_print() == 'DBEAFC'


def test_pre_order_empty_tree():
    tree = BinaryTree()
    assert tree.pre_order_print() == 'An emptey tree'

def test_in_order_empty_tree():
    tree = BinaryTree()
    assert tree.in_order_print() == 'An emptey tree'

def test_post_order_empty_tree():
    tree = BinaryTree()
    assert tree.post_order_print() == 'An emptey tree'


def test_instantiate_an_empty_tree():
    tree= BinarySearchTree()
    assert tree.root == None

def test_instantiate_tree_with_single_root():
    tree= BinarySearchTree()
    tree.insert(2)
    assert tree.pre_order_print() == '2'


def test_contains_False():
    tree= BinarySearchTree()
    tree.insert(9)
    tree.insert(2)
    tree.insert(3)
    assert tree.find(8) == False

def test_contains_True():
    tree= BinarySearchTree()
    tree.insert(9)
    tree.insert(2)
    tree.insert(3)
    assert tree.find(2) == True


@pytest.fixture
def prepared_tree():
    tree = BinaryTree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree