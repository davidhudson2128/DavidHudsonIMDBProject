import sqlite3
# import json
from typing import Tuple
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
        curser.execute('''CREATE TABLE "Top250Data" (
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


def create_db_columns_user_ratings(curser):
    # try:
    curser.execute('''CREATE TABLE "UserRatings" (
        "imdb_id"	INTEGER,
        "total_rating"	INTEGER,
        "total_rating_votes"    INTEGER,
        "rating_percent_10"	INTEGER,
        "rating_votes_10"	INTEGER,
        "rating_percent_9"	INTEGER,
        "rating_votes_9"	INTEGER,
        "rating_percent_8"	INTEGER,
        "rating_votes_8"	INTEGER,
        "rating_percent_7"	INTEGER,
        "rating_votes_7"	INTEGER,
        "rating_percent_6"	INTEGER,
        "rating_votes_6"	INTEGER,
        "rating_percent_5"	INTEGER,
        "rating_votes_5"	INTEGER,
        "rating_percent_4"	INTEGER,
        "rating_votes_4"	INTEGER,
        "rating_percent_3"	INTEGER,
        "rating_votes_3"	INTEGER,
        "rating_percent_2"	INTEGER,
        "rating_votes_2"	INTEGER,
        "rating_percent_1"	INTEGER,
        "rating_votes_1"	INTEGER,
        FOREIGN KEY("imdb_id") REFERENCES "Top250Data"("id")
    );''')
    # Database already created
    # except sqlite3.OperationalError as e:
    #     pass


def write_data_to_db_top250(curser, top_250_shows_data):

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

    print(ratings_data)
    for show_data in ratings_data:
        print(show_data.get('ratings'))
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


def main(top_250_shows_data, user_ratings_data):
    conn_top250, cursor_top250 = open_db("top_250_shows_db.sqlite")
    create_db_columns_top250(cursor_top250)
    write_data_to_db_top250(cursor_top250, top_250_shows_data)

    conn_user_ratings, cursor_user_ratings = open_db("user_ratings_db.sqlite")
    create_db_columns_user_ratings(cursor_user_ratings)
    write_data_to_db_user_ratings(cursor_user_ratings, user_ratings_data)

    close_db(conn_top250)
    close_db(conn_user_ratings)
