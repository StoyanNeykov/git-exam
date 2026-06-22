import pytest
from age_checker import is_adult


@pytest.mark.parametrize(
    "age, expected",
    [(17, False)],
)
def test_is_adult(age, expected):
    assert is_adult(age) == expected
