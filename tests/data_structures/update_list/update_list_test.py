import pytest

from tasks.data_structures.update_list.solution import solution, Node

def test_remove_middle():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.value == "node0"
    assert new_head.next_item is node2
    assert new_head.next_item.value == "node2"
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.value == "node3"
    assert new_head.next_item.next_item.next_item is None

def test_remove_first():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    assert new_head is node1
    assert new_head.value == "node1"
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None

def test_remove_last():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 3)
    assert new_head is node0
    assert new_head.next_item is node1
    assert new_head.next_item.next_item is node2
    assert new_head.next_item.next_item.next_item is None

def test_remove_single():
    node0 = Node("node0", None)
    new_head = solution(node0, 0)
    assert new_head is None

def test_remove_second_in_three():
    node2 = Node("node2", None)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is None

def test_large_list_remove():
    head = Node(0)
    current = head
    for i in range(1, 5000):
        current.next_item = Node(i)
        current = current.next_item
    new_head = solution(head, 2500)
    assert new_head.value == 0
    current = new_head
    count = 0
    while current:
        count += 1
        current = current.next_item
    assert count == 4999