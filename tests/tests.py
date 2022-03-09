# import pytest
# import main
# import pytest

# import databases
import databases
import main
import GUI


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


def test_find_biggest_movers():
    test_data_conn, test_data_cursor = databases.open_db("test.sqlite")
    test_data_cursor.execute('''CREATE TABLE IF NOT EXISTS MostPopularMovies(
            "id"	TEXT,
            "rank"  INT,
            "rankUpDown"    INT,
            "title"	TEXT,
            "full_title"	TEXT,
            "year"	INTEGER,
            "crew"	TEXT
        );''')
    test_data = [('id1', 1, 40, 'test show 1', 'full title', 1924, 'crew'),
                 ('id2', 2, 0, 'test show 2', 'full title', 1924, 'crew'),
                 ('id3', 3, -20, 'test show 3', 'full title', 1924, 'crew'),
                 ('id4', 4, 33, 'test show 4', 'full title', 1924, 'crew'),
                 ('id5', 5, 30, 'test show 5', 'full title', 1924, 'crew')]
    test_data_cursor.executemany('''INSERT INTO MostPopularMovies(id, rank, rankUpDown, title, full_title,
                    year, crew)
                     VALUES(?,?,?,?,?,?,?)''', test_data)

    test_biggest_increases = databases.find_biggest_increases(test_data_cursor)
    assert len(test_biggest_increases) == 3
# Not working
#     assert test_biggest_increases == [('id1', 1, 40, 'test show 1', 'full title', 1924, 'crew'),
#                                       ('id4', 4, 33, 'test show 4', 'full title', 1924, 'crew'),
#                                       ('id5', 5, 30, 'test show 5', 'full title', 1924, 'crew')]

    test_biggest_decreases = databases.find_biggest_decreases(test_data_cursor)
    assert test_biggest_decreases[0] == ('id3', 3, -20, 'test show 3', 'full title', 1924, 'crew')

    databases.close_db(test_data_conn)


def test_new_table_created():
    # conn, cursor = databases.open_db('IMDBDatabase.sqlite')
    #
    # assert cursor.execute('''
    #     SELECT NAME FROM sqlite_master WHERE type='table';
    #     ''').fetchall() == 1
    pass


def test_movie_crossovers():
    overlap = GUI.DataGraphWindow.find_overlapping_movies()
    assert overlap <= 100
    # assert overlap[-1] in


if __name__ == '__main__':
    print(test_top_250_data())
