import pytest
from pythoncalculator import divide


def test_divide():
    with pytest.raises(NameError):
        divide(10, 2)
