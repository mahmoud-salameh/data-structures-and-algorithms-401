import pytest
from hashmap_tree_intersection.hashmap_tree_intersection import *

def test_happy_path(prepared_tree1,prepared_tree2):

    actual=intersection(prepared_tree1,prepared_tree2)
    expected=[1, 11, 13, 2, 23, 4]
    assert actual==expected



def test_edge_case():
    tree1=BinaryTree()
    tree2=BinaryTree()
    actual=intersection(tree1,tree2)
    expected='The trees are empty'
    
    assert actual==expected


def test_expected_failure(prepared_tree1,prepared_tree2):
    prepared_tree1.root.left=Node(600)
    actual=intersection(prepared_tree1,prepared_tree2)
    expected=[4,1,13,11,2]
    assert actual!=expected

        #                  7
        #                /   \
        #              4       11
        #             / \       \
        #            1   13       19
        #                 \      /
        #                  23    2

        #                  9
        #                /   \
        #              1       23
        #             / \       \
        #            24   11     4
        #           /    /   \      
        #          21    13   2   


@pytest.fixture
def prepared_tree1():
    tree1=BinaryTree()
    tree1.root=Node(7)
    tree1.root.left=Node(4)
    tree1.root.left.left=Node(1)
    tree1.root.left.right=Node(13)
    tree1.root.left.right.right=Node(23)
    tree1.root.right=Node(11)
    tree1.root.left.left=Node(1)
    tree1.root.right.right=Node(19)
    tree1.root.right.right.left=Node(2)
 
    return tree1


        #                  9
        #                /   \
        #              1       23
        #             / \       \
        #            24   11     4
        #           /    /   \      
        #          21    13   2   
@pytest.fixture
def prepared_tree2():
    tree2=BinaryTree()
    tree2.root=Node(9)
    tree2.root.left=Node(1)
    tree2.root.left.left=Node(24)
    tree2.root.left.right=Node(11)
    tree2.root.left.left.left=Node(21)
    tree2.root.left.right.left=Node(13)
    tree2.root.left.right.right=Node(2)
    tree2.root.right=Node(23)
    tree2.root.right.right=Node(4)

    return tree2