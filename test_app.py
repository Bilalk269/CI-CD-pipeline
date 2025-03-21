import pytest
from app  import add


def test_add():
    assert add(2,3) == 5
    assert add(3,3) == 6
    assert add(0,0) == 1