import json
import sqlite3
# import json
from typing import Tuple
# import requests
# import
# import requests


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def create_db_columns_top250(curser):
    try:
        curser.execute('''CREATE TABLE IF NOT EXISTS "Top250Data" (
            "id"	TEXT,
            "title"	TEXT,
            "full_title"	INTEGER,
            "year"	INTEGER,
            "crew"	TEXT,
            "imdb_rating"	NUMERIC,
            "imdb_rating_count"	INTEGER,
            PRIMARY KEY("id")
        );''')
    # Database already created
    except sqlite3.OperationalError:
        pass


def create_db_columns_top250_movies(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS "Top250MoviesData" (
                "id"	TEXT,
                "title"	TEXT,
                "full_title"	INTEGER,
                "year"	INTEGER,
                "crew"	TEXT,
                "imdb_rating"	NUMERIC,
                "imdb_rating_count"	INTEGER,
                PRIMARY KEY("id")
            );''')


def create_db_columns_user_ratings(curser):
    # try:
    curser.execute('''CREATE TABLE IF NOT EXISTS UserRatings(
        "imdb_id"	TEXT,
        "total_rating"	TEXT,
        "total_rating_votes"    TEXT,
        "rating_percent_10"	TEXT,
        "rating_votes_10"	TEXT,
        "rating_percent_9"	TEXT,
        "rating_votes_9"	TEXT,
        "rating_percent_8"	TEXT,
        "rating_votes_8"	TEXT,
        "rating_percent_7"	TEXT,
        "rating_votes_7"	TEXT,
        "rating_percent_6"	TEXT,
        "rating_votes_6"	TEXT,
        "rating_percent_5"	TEXT,
        "rating_votes_5"	TEXT,
        "rating_percent_4"	TEXT,
        "rating_votes_4"	TEXT,
        "rating_percent_3"	TEXT,
        "rating_votes_3"	TEXT,
        "rating_percent_2"	TEXT,
        "rating_votes_2"	TEXT,
        "rating_percent_1"	TEXT,
        "rating_votes_1"	TEXT,
        FOREIGN KEY("imdb_id") REFERENCES "Top250Data"("id")
    );''')
    # Database already created
    # except sqlite3.OperationalError as e:
    #     pass


def create_db_columns_most_popular_shows(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS MostPopularShows(
            "id"	TEXT,
            "rank"  INTEGER,
            "rankUpDown"    INT,
            "title"	TEXT,
            "full_title"	TEXT,
            "year"	INTEGER,
            "crew"	TEXT,
            PRIMARY KEY("id")
        );''')


def create_db_columns_most_popular_movies(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS MostPopularMovies(
            "id"	TEXT,
            "rank"  INTEGER,
            "rankUpDown"    INT,
            "title"	TEXT,
            "full_title"	TEXT,
            "year"	INTEGER,
            "crew"	TEXT,
            PRIMARY KEY("id")
        );''')


def create_db_columns_most_highest_movers_movies(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS HighestMoversMovies(
            "id"	TEXT,
            "rank"  INTEGER,
            "rankUpDown"    INT,
            "title"	TEXT,
            "full_title"	TEXT,
            "year"	INTEGER,
            "crew"	TEXT,
            PRIMARY KEY("id")
        );''')


def write_data_to_db_most_popular_shows(cursor):
    with open("secrets.py", "r") as secret_file:
        imdb_api_key = secret_file.read()
        imdb_api_key = "k_ul3l4k74"

    # most_popular_shows_request = requests.get(f'https://imdb-api.com/en/API/MostPopularTVs/{imdb_api_key}')
    # most_popular_shows_data = most_popular_shows_request.json().get('items')
    #
    # with open("json data/most_popular_shows.json", "w") as file:
    #     file.write(json.dumps(most_popular_shows_data))
    # read data from file
    with open("json data/most_popular_shows.json", "r") as file:
        most_popular_shows_data = json.load(file)

    for show in most_popular_shows_data:
        # print(show)

        cursor.execute(f'''INSERT INTO MostPopularShows(id, rank, rankUpDown, title, full_title,
                        year, crew)
                         VALUES ('{show.get('id')}',
                         '{show.get('rank')}',
                         '{int(show.get('rankUpDown').replace(",", ""))}',
                         '{show.get('title').replace("'", "")}',
                         '{show.get('fullTitle').replace("'", "")}',
                         '{show.get('year')}',
                         '{show.get('crew').replace("'", "")}'
                         )''')


def write_data_to_db_most_popular_movies(cursor):
    with open("secrets.py", "r") as secret_file:
        imdb_api_key = secret_file.read()
        imdb_api_key = "k_ul3l4k74"

    # most_popular_movies_request = requests.get(f'https://imdb-api.com/en/API/MostPopularMovies/{imdb_api_key}')
    # most_popular_movies_data = most_popular_movies_request.json().get('items')
    #
    # with open("json data/most_popular_movies.json", "w") as file:
    #     file.write(json.dumps(most_popular_movies_data))
    # read data from file
    with open("json data/most_popular_movies.json", "r") as file:
        most_popular_movies_data = json.load(file)

    for movie in most_popular_movies_data:
        # print(show)

        cursor.execute(f'''INSERT INTO MostPopularMovies(id, rank, rankUpDown, title, full_title,
                        year, crew)
                         VALUES ('{movie.get('id')}',
                         '{movie.get('rank')}',
                         '{int(movie.get('rankUpDown').replace(",", ""))}',
                         '{movie.get('title').replace("'", "")}',
                         '{movie.get('fullTitle').replace("'", "")}',
                         '{movie.get('year')}',
                         '{movie.get('crew').replace("'", "")}'
                         )''')


def write_data_to_db_top250_movies(cursor):
    with open("secrets.py", "r") as secret_file:
        imdb_api_key = secret_file.read()
        imdb_api_key = "k_ul3l4k74"
    # top_250_movies_request = requests.get(f'https://imdb-api.com/en/API/Top250Movies/{imdb_api_key}')
    # top_250_movies_data = top_250_movies_request.json().get('items')
    #
    # with open("json data/top_250_movies.json", "w") as file:
    #     file.write(json.dumps(top_250_movies_data))
    # read data from file
    with open("json data/top_250_movies.json", "r") as file:
        top_250_movies_data = json.load(file)

    for movie in top_250_movies_data:
        cursor.execute(f'''INSERT INTO Top250MoviesData(id, title, full_title,
                        year, crew, imdb_rating, imdb_rating_count)
                         VALUES ('{movie.get('id')}',
                         '{movie.get('title').replace("'", "")}',
                         '{movie.get('fullTitle').replace("'", "")}',
                         '{movie.get('year')}',
                         '{movie.get('crew').replace("'", "")}',
                         '{movie.get('imDbRating')}',
                         '{movie.get('imDbRatingCount')}')''')


def write_data_to_db_top250_shows(curser, top_250_shows_data):
    # try:

    # Add Shows 1, 50,101, 200 to Database
    list_of_show_indexes_to_add = [0, 49, 99, 199]
    for show_index in list_of_show_indexes_to_add:
        curser.execute(f'''INSERT INTO Top250Data(id, title, full_title,
                year, crew, imdb_rating, imdb_rating_count)
                 VALUES ('{top_250_shows_data.get('items')[show_index].get('id')}',
                 '{top_250_shows_data.get('items')[show_index].get('title')}',
                 '{top_250_shows_data.get('items')[show_index].get('fullTitle')}',
                 '{top_250_shows_data.get('items')[show_index].get('year')}',
                 '{top_250_shows_data.get('items')[show_index].get('crew')}',
                 '{top_250_shows_data.get('items')[show_index].get('imDbRating')}',
                 '{top_250_shows_data.get('items')[show_index].get('imDbRatingCount')}')''')

    # Get Wheel of Time data
    # with open("secret_api_key.txt", "r") as secret_file:
    #     api_key = secret_file.read()
    # wheel_of_time_data = requests.get(f'https://imdb-api.com/en/API/Report/{api_key}/tt7462410').json()

    # with open('wheel_of_time_data.json', 'w') as file:
    #     file.write(json.dumps(wheel_of_time_data))
    # with open('wheel_of_time_data.json', 'r') as file:
    #     wheel_of_time_data = json.load(file)

    # print(wheel_of_time_data)

    # Add Wheel of Time to db


#     curser.execute(f'''INSERT INTO Top250Data(id, title, full_title,
#                 year, crew, imdb_rating, imdb_rating_count)
#                  VALUES ('{top_250_shows_data.get('items')[show_index].get('id')}', '{top_250_shows_data.get('items')
#                  [show_index].get('title')}', '{top_250_shows_data.get('items')[show_index].get('fullTitle')}',
#                  '{top_250_shows_data.get('items')[show_index].get('year')}',
#                  '{top_250_shows_data.get('items')[show_index].get('crew')}',
#                  '{top_250_shows_data.get('items')[show_index].get('imDbRating')}',
#                  '{top_250_shows_data.get('items')[show_index].get('imDbRatingCount')}')''')
# )

# Primary key not unique
# except sqlite3.IntegrityError:
#     print("b")


def write_data_to_db_user_ratings(cursor, ratings_data):
    # print(ratings_data)
    for show_data in ratings_data:
        # print(show_data.get('ratings'))
        cursor.execute(f'''INSERT INTO UserRatings(imdb_id, total_rating, total_rating_votes,
                         rating_percent_10, rating_votes_10, rating_percent_9, rating_votes_9, rating_percent_8,
                         rating_votes_8, rating_percent_7, rating_votes_7, rating_percent_6, rating_votes_6,
                         rating_percent_5, rating_votes_5, rating_percent_4, rating_votes_4, rating_percent_3,
                         rating_votes_3, rating_percent_2, rating_votes_2, rating_percent_1, rating_votes_1)
                         VALUES ('{show_data.get('imDbId')}', '{show_data.get('totalRating')}',
                         '{show_data.get('totalRatingVotes')}', '{show_data.get('ratings')[0].get('percent')}',
                         '{show_data.get('ratings')[0].get('votes')}', '{show_data.get('ratings')[1].get('percent')}',
                         '{show_data.get('ratings')[1].get('votes')}', '{show_data.get('ratings')[2].get('percent')}',
                         '{show_data.get('ratings')[2].get('votes')}', '{show_data.get('ratings')[3].get('percent')}',
                         '{show_data.get('ratings')[3].get('votes')}', '{show_data.get('ratings')[4].get('percent')}',
                         '{show_data.get('ratings')[4].get('votes')}', '{show_data.get('ratings')[5].get('percent')}',
                         '{show_data.get('ratings')[5].get('votes')}', '{show_data.get('ratings')[6].get('percent')}',
                         '{show_data.get('ratings')[6].get('votes')}', '{show_data.get('ratings')[7].get('percent')}',
                         '{show_data.get('ratings')[7].get('votes')}', '{show_data.get('ratings')[8].get('percent')}',
                         '{show_data.get('ratings')[8].get('votes')}', '{show_data.get('ratings')[9].get('percent')}',
                         '{show_data.get('ratings')[9].get('votes')}')''')


def write_data_to_db_highest_movers_movies(cursor):
    biggest_increases = []
    biggest_decreases = []

    conn_most_popular_movies, cursor_most_popular_movies = open_db("most_popular_movies_db.sqlite")
    movies_sorted_by_rankUpDown = cursor_most_popular_movies.execute('''
    SELECT * FROM MostPopularMovies ORDER BY rankUpDown DESC;
    ''').fetchall()
    biggest_increases.append(movies_sorted_by_rankUpDown[0])
    biggest_increases.append(movies_sorted_by_rankUpDown[1])
    biggest_increases.append(movies_sorted_by_rankUpDown[2])
    biggest_decreases.append(movies_sorted_by_rankUpDown[-1])

    for movie in biggest_increases:
        cursor.execute(f'''INSERT INTO HighestMoversMovies(id, rank, rankUpDown, title, full_title,
                            year, crew)
                             VALUES ('{movie[0]}',
                             '{movie[1]}',
                             '{int(movie[2])}',
                             '{movie[3]}',
                             '{movie[4]}',
                             '{movie[5]}',
                             '{movie[6]}'
                             )''')
    for movie in biggest_decreases:
        cursor.execute(f'''INSERT INTO HighestMoversMovies(id, rank, rankUpDown, title, full_title,
                            year, crew)
                             VALUES ('{movie[0]}',
                             '{movie[1]}',
                             '{int(movie[2])}',
                             '{movie[3]}',
                             '{movie[4]}',
                             '{movie[5]}',
                             '{movie[6]}'
                             )''')


def main(top_250_shows_data, user_ratings_data):
    conn_top250_shows, cursor_top250_shows = open_db("top_250_shows_db.sqlite")
    create_db_columns_top250(cursor_top250_shows)
    write_data_to_db_top250_shows(cursor_top250_shows, top_250_shows_data)

    conn_user_ratings, cursor_user_ratings = open_db("user_ratings_db.sqlite")
    create_db_columns_user_ratings(cursor_user_ratings)
    write_data_to_db_user_ratings(cursor_user_ratings, user_ratings_data)

    conn_most_popular_shows, cursor_most_popular_shows = open_db("most_popular_shows_db.sqlite")
    create_db_columns_most_popular_shows(cursor_most_popular_shows)
    write_data_to_db_most_popular_shows(cursor_most_popular_shows)

    conn_top250_movies, cursor_top250_movies = open_db("top_250_movies_db.sqlite")
    create_db_columns_top250_movies(cursor_top250_movies)
    write_data_to_db_top250_movies(cursor_top250_movies)

    conn_most_popular_movies, cursor_most_popular_movies = open_db("most_popular_movies_db.sqlite")
    create_db_columns_most_popular_movies(cursor_most_popular_movies)
    write_data_to_db_most_popular_movies(cursor_most_popular_movies)

    close_db(conn_top250_shows)
    close_db(conn_user_ratings)
    close_db(conn_most_popular_shows)
    close_db(conn_top250_movies)
    close_db(conn_most_popular_movies)

    conn_highest_movers_movies, cursor_highest_movers_movies = open_db("highest_movers_db.sqlite")
    create_db_columns_most_highest_movers_movies(cursor_highest_movers_movies)
    write_data_to_db_highest_movers_movies(cursor_highest_movers_movies)
    close_db(conn_highest_movers_movies)
