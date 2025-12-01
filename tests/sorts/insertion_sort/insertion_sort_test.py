import pytest

from tasks.sorts.insertion_sort.solution import insertion_sort

def test_empty_array():
    assert insertion_sort([]) == []

def test_single_element():
    assert insertion_sort([3]) == [3]

def test_random_array():
    assert insertion_sort([9, 5, 1, 4, 3]) == [1, 3, 4, 5, 9]

def test_reverse_sorted():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_with_negatives_and_duplicates():
    assert insertion_sort([2, -1, 2, -1, 0]) == [-1, -1, 0, 2, 2]

def test_already_sorted():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_single_large_element():
    assert insertion_sort([10]) == [10]

def test_extremes():
    assert insertion_sort([1000, -1000, 0]) == [-1000, 0, 1000]