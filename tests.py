import pytest

from stack_main import check_brackets


@pytest.mark.parametrize(
    "brackets,expected",
    [
        ("(((([{}]))))", True),
        ("[([])((([[[]]])))]{()}", True),
        ("{{[()]}}", True),
        ("}{}", False),
        ("{{[(])]}}", False),
        ("[[{())}]", False),
    ],
)
def test_check_brackets(brackets, expected):
    assert check_brackets(brackets) == expected
