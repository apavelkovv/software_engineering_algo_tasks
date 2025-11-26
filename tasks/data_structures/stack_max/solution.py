class StackMax:
    """Стек с операцией получения максимума за O(1)."""

    def __init__(self) -> None:
        """Инициализирует стеки: основной и для максимумов."""
        self.stack: list[int] = []
        self.max_stack: list[int] = []

    def push(self, x: int) -> None:
        """Добавляет элемент и обновляет максимум.

        Args:
            x: целое число
        """
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self) -> int | str:
        """Удаляет и возвращает верхний элемент.

        Returns:
            "error" если пуст, иначе элемент
        """
        if not self.stack:
            return "error"

        popped = self.stack.pop()
        if self.max_stack and popped == self.max_stack[-1]:
            self.max_stack.pop()
        return popped

    def get_max(self) -> int | None:
        """Возвращает максимум.

        Returns:
            None если пуст, иначе максимум
        """
        if not self.max_stack:
            return None
        return self.max_stack[-1]