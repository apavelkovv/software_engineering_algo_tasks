class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

def solution(node: Node, idx: int) -> Node:
    if idx == 0:
        return node.next_item
    current = node
    for _ in range(idx - 1):
        if current is None:
            return node
        current = current.next_item
    if current and current.next_item:
        current.next_item = current.next_item.next_item
    return node