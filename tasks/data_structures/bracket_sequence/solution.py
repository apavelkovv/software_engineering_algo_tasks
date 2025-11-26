def is_correct_bracket_seq(s: str) -> bool:
    """Проверяет, является ли строка правильной скобочной последовательностью.

    Args:
        s: строка, содержащая только символы ()[]{}

    Returns:
        True если последовательность правильная, иначе False

    Time: O(n), Space: O(n)
    """
    if not s:
        return True

    # Маппинг закрывающихся скобок на открывающиеся
    bracket_map = {')': '(', ']': '[', '}': '{'}
    # Кэшируем открывающиеся скобки в set для O(1) поиска
    opening_brackets = set(bracket_map.values())

    stack: list[str] = []

    for char in s:
        if char in opening_brackets:
            # Открывающаяся скобка — добавляем в стек
            stack.append(char)
        elif char in bracket_map:
            # Закрывающаяся скобка — проверяем соответствие
            if not stack or stack.pop() != bracket_map[char]:
                return False

    # Если стек пуст — все скобки закрыты корректно
    return len(stack) == 0