from quick_sort.quick_sort import *

def test_quick_sort():
    arr =[8,4,23,42,16,15]
    actual= quick_sort(arr,0,len(arr)-1)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_reverse_sorted():
    arr =[20,18,12,8,5,-2]
    actual= quick_sort(arr,0,len(arr)-1)
    expected = [-2,5,8,12,18,20]
    assert actual == expected


def test_few_uniques(): 
    arr =[5,12,7,5,5,7]
    actual= quick_sort(arr,0,len(arr)-1)
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_nearly_sorted():
    arr =[2,3,5,7,13,11]
    actual= quick_sort(arr,0,len(arr)-1)
    expected = [2,3,5,7,11,13]
    assert actual == expected