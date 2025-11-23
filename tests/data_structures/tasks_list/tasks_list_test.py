import pytest
from io import StringIO

from tasks.data_structures.tasks_list.solution import solution, Node

def test_print_four_nodes(capsys):
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    captured = capsys.readouterr()
    assert captured.out == "node0\nnode1\nnode2\nnode3\n"

def test_print_single_node(capsys):
    node = Node("single", None)
    solution(node)
    captured = capsys.readouterr()
    assert captured.out == "single\n"

def test_print_two_nodes(capsys):
    node1 = Node("node1", None)
    node0 = Node("node0", node1)
    solution(node0)
    captured = capsys.readouterr()
    assert captured.out == "node0\nnode1\n"

def test_print_three_nodes(capsys):
    node2 = Node("node2", None)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    captured = capsys.readouterr()
    assert captured.out == "node0\nnode1\nnode2\n"

def test_print_five_nodes(capsys):
    node4 = Node("node4", None)
    node3 = Node("node3", node4)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    captured = capsys.readouterr()
    assert captured.out == "node0\nnode1\nnode2\nnode3\nnode4\n"

def test_large_list(capsys):
    head = Node(0)
    current = head
    for i in range(1, 5000):
        current.next_item = Node(i)
        current = current.next_item
    solution(head)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert len(lines) == 5000
    assert lines[0] == "0"
    assert lines[-1] == "4999"