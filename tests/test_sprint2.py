# import pytest
# import main
# import pytest

# import databases
import main

# with open("secrets.py", "r") as secret_file:
#     api_key = secret_file.read()
#
# print(f"key: {api_key}")


def test_example():
    assert 4 == 2 + 2


def test_top_250_data():
    top_250_data = main.get_top_250_shows()
    top_250_data_size = len(top_250_data.get('items'))

    assert top_250_data_size == 250


if __name__ == '__main__':
    print(test_top_250_data())
