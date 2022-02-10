<<<<<<< HEAD
<<<<<<< Updated upstream
# import pytest
=======
# import main
import pytest
>>>>>>> Stashed changes
=======
import pytest

import main

with open("../secret_api_key.txt", "r") as secret_file:
    api_key = secret_file.read()
>>>>>>> 5a1d9152d6cf21c8395244b2e5ebbeafcc143a77


@pytest.fixture
def add():
    return 1+1


def test_example():
<<<<<<< Updated upstream
    assert 4 == add(2+2)


def test_top_250_data():
    top_250_data = main.get_top_250_shows(api_key)
    top_250_data_size = len(top_250_data.get('items'))
    assert top_250_data_size == 250

if __name__ == '__main__':
    print(test_top_250_data())
=======
    assert 4 == 4
>>>>>>> Stashed changes
