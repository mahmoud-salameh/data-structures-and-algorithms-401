from merge_sort.merge_sort import *


def test_Reverse_sorted():
    arr = [20,18,12,8,5,-2]
    merge_sort(arr)
    assert arr[0] == -2
    assert arr[1] == 5
    assert arr[-1] == 20

def test_Few_uniques():
    arr = [5,12,7,5,5,7]
    merge_sort(arr)
    assert arr[0] == 5
    assert arr[1] == 5
    assert arr[-1] == 12

def test_Nearly_sorted():
    arr = [2,3,5,7,13,11]
    merge_sort(arr)
    assert arr[2] == 5
    assert arr[3] == 7
    assert arr[4] == 11