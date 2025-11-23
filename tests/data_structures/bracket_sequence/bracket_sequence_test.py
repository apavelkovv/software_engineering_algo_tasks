import pytest

from tasks.data_structures.bracket_sequence.solution import is_correct_bracket_seq

def test_correct_sequences():
    assert is_correct_bracket_seq("{[()]}") is True
    assert is_correct_bracket_seq("()") is True
    assert is_correct_bracket_seq("") is True
    assert is_correct_bracket_seq("([]){}") is True
    assert is_correct_bracket_seq("((()))[]{}") is True

def test_incorrect_sequences():
    assert is_correct_bracket_seq("{[(]}") is False
    assert is_correct_bracket_seq("([)") is False
    assert is_correct_bracket_seq(")") is False
    assert is_correct_bracket_seq("(") is False
    assert is_correct_bracket_seq("}{") is False

def test_edge_cases():
    assert is_correct_bracket_seq("[]") is True
    assert is_correct_bracket_seq("{}") is True
    assert is_correct_bracket_seq("()[]{}") is True
    assert is_correct_bracket_seq("([{}])") is True
    assert is_correct_bracket_seq("(((") is False