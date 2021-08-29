from insertions.insertion_sort import *
import pytest



def test_random_sorted():
    arr=[8,4,23,42,16,15]
    insertion_sort(arr)
    assert arr[0]==4
    assert arr[1]==8
    assert arr[-1]==42

def test_Reverse_sorted():
    arr=[8,4,23,42,16,15]
    insertion_sort(arr)
    assert arr[2] == 15
    assert arr[3] == 16
    assert arr[4] == 23

def test_Few_uniques():
    arr=[8,4,23,8,8,23]
    insertion_sort(arr)
    assert arr[0] == 4
    assert arr[1] == 8
    assert arr[-1] == 23

def test_Nearly_sorted():
    arr = [4,8,16,15,23,42]
    insertion_sort(arr)
    assert arr[0] == 4
    assert arr[1] == 8
    assert arr[-1] == 42