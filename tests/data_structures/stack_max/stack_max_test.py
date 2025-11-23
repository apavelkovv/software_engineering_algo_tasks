import pytest

from tasks.data_structures.stack_max.solution import StackMax

def test_empty_stack():
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"

def test_basic_operations():
    stack = StackMax()
    stack.push(7)
    assert stack.get_max() == 7
    stack.push(1)
    stack.push(3)
    assert stack.get_max() == 7
    stack.pop()
    stack.pop()
    assert stack.get_max() == 7
    stack.pop()
    assert stack.get_max() == "None"

def test_duplicate_max():
    stack = StackMax()
    stack.push(5)
    stack.push(5)
    assert stack.get_max() == 5
    stack.pop()
    assert stack.get_max() == 5
    stack.pop()
    assert stack.get_max() == "None"

def test_increasing_max():
    stack = StackMax()
    stack.push(10)
    stack.push(-1)
    stack.push(20)
    assert stack.get_max() == 20
    stack.pop()
    assert stack.get_max() == 10
    stack.pop()
    assert stack.get_max() == 10
    stack.pop()
    assert stack.get_max() == "None"

def test_large_stack():
    stack = StackMax()
    for i in range(10000):
        stack.push(i)
    assert stack.get_max() == 9999
    for i in range(5000):
        stack.pop()
    assert stack.get_max() == 4999
    for i in range(5000):
        stack.pop()
    assert stack.get_max() == "None"

def test_negative_numbers():
    stack = StackMax()
    stack.push(-10)
    stack.push(-20)
    stack.push(-5)
    assert stack.get_max() == -5
    stack.pop()
    assert stack.get_max() == -10
    stack.pop()
    assert stack.get_max() == -10
    stack.pop()
    assert stack.get_max() == "None"