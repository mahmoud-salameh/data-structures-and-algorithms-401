from trees.binary_max_tree import *
import pytest



         #                  7
         #                /   \
         #              4       11
         #             / \     / \
         #            1   13       19
         #               / \     /
         #              9   23  14




def test_max_happy_path(pre_order_tree):
    assert pre_order_tree.max_in_tree() == 23

def test_max_expected_failure(pre_order_tree):
    assert pre_order_tree.max_in_tree() != 19

def test_edge_Case(pre_order_tree):
    pre_order_tree.root = Node(28)
    assert pre_order_tree.max_in_tree() == 28
  
@pytest.fixture
def pre_order_tree():
    tree = BinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(4)
    tree.root.right = Node(11)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(13)
    tree.root.left.right.right = Node(23)
    tree.root.right.right = Node(19)

    return tree


         
                   