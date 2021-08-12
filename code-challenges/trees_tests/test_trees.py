from trees.binary_tree import *
import pytest


def test_pre_order(fixed_tree):
    assert fixed_tree.pre_order() == 'ABDECF'


def test_post_order(fixed_tree):
    assert fixed_tree.post_order() == 'DEBFCA'

def test_in_order(fixed_tree):
    assert fixed_tree.in_order() == 'DBEAFC'


def test_pre_order_empty_tree():
    tree = BinaryTree()
    assert tree.pre_order() == 'An emptey tree'

def test_in_order_empty_tree():
    tree = BinaryTree()
    assert tree.in_order() == 'An emptey tree'

def test_post_order_empty_tree():
    tree = BinaryTree()
    assert tree.post_order() == 'An emptey tree'


@pytest.fixture
def fixed_tree():
    tree = BinaryTree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree