class Node:
    """Узел односвязного списка."""

    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

def solution(node: Node, idx: int) -> Node | None:
    """Удаляет элемент из односвязного списка по индексу.

    Args:
        node: голова списка
        idx: индекс удаляемого элемента (0-индексация)

    Returns:
        голова обновлённого списка (или None если список пуст или idx=0 и single)

    Time: O(n), Space: O(1)
    """
    if not node or idx < 0:
        return node

    # Удаление первого элемента
    if idx == 0:
        return node.next_item

    # Поиск узла перед удаляемым
    current = node
    for _ in range(idx - 1):
        if current is None or current.next_item is None:
            return node
        current = current.next_item

    # Проверка, что узел и следующий узел существуют
    if current is not None and current.next_item is not None:
        current.next_item = current.next_item.next_item

    return node