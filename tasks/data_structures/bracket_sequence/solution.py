def is_correct_bracket_seq(s: str) -> bool:
    if not s:
        return True

    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            return False

    return len(stack) == 0