import pytest
from age_checker import is_adult


@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (19, True),
        (0, False),
        (100, True),
    ],
)
def test_is_adult(age, expected):
    assert is_adult(age) == expected
