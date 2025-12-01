import pytest

from tasks.recursion.binary_search.solution import binary_search

def test_found_in_duplicates():
    arr = [1, 2, 2, 4, 7]
    result = binary_search(arr, 2)
    assert result in (1, 2)

def test_not_found():
    arr = [1, 3, 5]
    assert binary_search(arr, 2) == -1

def test_empty_array():
    assert binary_search([], 10) == -1

def test_single_element_found():
    assert binary_search([5], 5) == 0

def test_single_element_not_found():
    assert binary_search([5], 10) == -1

def test_first_element():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 1) == 0

def test_last_element():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 5) == 4

def test_large_array():
    arr = list(range(1000000))
    assert binary_search(arr, 999999) == 999999
    assert binary_search(arr, -1) == -1