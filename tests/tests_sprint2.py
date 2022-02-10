# import main
import pytest


@pytest.fixture
def add():
    return 1+1


def test_test():
    assert 5 == 4
