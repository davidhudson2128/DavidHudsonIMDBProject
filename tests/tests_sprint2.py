# import main
import pytest


@pytest.fixture
def add():
    return 1+1


def test_example():
    assert 5 == 4
