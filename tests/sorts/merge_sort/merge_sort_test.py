import pytest

from tasks.sorts.merge_sort.solution import merge_sort

def test_empty_array():
    assert merge_sort([]) == []

def test_single_element():
    assert merge_sort([3]) == [3]

def test_reverse_sorted():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_with_negatives_and_duplicates():
    assert merge_sort([2, -1, 2, -1, 0]) == [-1, -1, 0, 2, 2]

def test_random_array():
    assert merge_sort([4, 5, 3, 0, 1, 2]) == [0, 1, 2, 3, 4, 5]

def test_already_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negatives():
    assert merge_sort([-10, -5, 0, 5, 10]) == [-10, -5, 0, 5, 10]

def test_all_equal():
    assert merge_sort([1] * 100) == [1] * 100