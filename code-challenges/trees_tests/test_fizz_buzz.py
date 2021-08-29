from trees.fizz_buzz import *
import pytest

def test_fizz(prepared_kAryTree):
    fizz_buzz_tree(prepared_kAryTree)
    assert prepared_kAryTree.root.result != 'buzz'

def test_buzz(prepared_kAryTree):
    fizz_buzz_tree(prepared_kAryTree)
    assert prepared_kAryTree.root.result[0].result != 'fizz'

def test_tree_fizz_buzz_happy_path(prepared_kAryTree):
    fizz_buzz_tree(prepared_kAryTree)
    assert prepared_kAryTree.root.result[2].result[1].result[2].value == 'Fizz Buzz'


def test_tree_fizz_buzz_Case(prepared_kAryTree):
    fizz_buzz_tree(prepared_kAryTree)
    assert type(prepared_kAryTree.root.value) == type('string') 


@pytest.fixture
def prepared_kAryTree():
    kAry = k_Ary()
    kAry.root = Node(1)
    kAry.root.result += [Node(2)]
    kAry.root.result += [Node(3)]
    kAry.root.result += [Node(4)]
    kAry.root.result[0].result += [Node(5)]
    kAry.root.result[0].result += [Node(6)]
    kAry.root.result[0].result += [Node(7)]
    kAry.root.result[1].result += [Node(8)]
    kAry.root.result[2].result += [Node(9)]
    kAry.root.result[2].result += [Node(10)]
    kAry.root.result[0].result[2].result += [Node(11)]
    kAry.root.result[0].result[2].result += [Node(12)]
    kAry.root.result[2].result[1].result += [Node(13)]
    kAry.root.result[2].result[1].result += [Node(14)]
    kAry.root.result[2].result[1].result += [Node(15)]

    return kAry