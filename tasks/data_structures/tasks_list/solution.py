class Node:
    """Узел односвязного списка."""

    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

def solution(node: Node) -> None:
    """Печатает все элементы односвязного списка по одному на строку.

    Args:
        node: голова списка

    Time: O(n), Space: O(1)
    """
    while node:
        print(node.value)
        node = node.next_item