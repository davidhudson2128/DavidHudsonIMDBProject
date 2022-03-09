import sqlite3
from typing import Tuple

import PySide6.Qt
import PySide6.QtWidgets
import matplotlib.pyplot as plt
import requests
import sys
from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QListWidgetItem, QLabel, QLineEdit


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor

def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()

def plot_data():

    conn, cursor = open_db("IMDBDatabase.sqlite")
    cursor.execute("""SELECT * FROM MostPopularMovies""")
    movie_data = cursor.fetchall()
    rankUpDown_values_movies = []
    number_decreasing_movies = 0
    number_increasing_movies = 0
    for entry in movie_data:
        if entry[2] < 0:
            number_decreasing_movies += 1
        elif entry[2] > 1:
            number_increasing_movies += 1
        rankUpDown_values_movies.append(entry[2])


    cursor.execute("""SELECT * FROM MostPopularShows""")
    tv_data = cursor.fetchall()
    close_db(conn)
    rankUpDown_values_tv = []
    number_decreasing_shows = 0
    number_increasing_shows = 0
    for entry in tv_data:
        if entry[2] < 0:
            number_decreasing_shows += 1
        elif entry[2] > 1:
            number_increasing_shows += 1
        if entry[2] <= 9000:
            rankUpDown_values_tv.append(entry[2])

    fig, axs = plt.subplots(2)

    axs[0].set_title("Most Popular Shows Movement")
    axs[0].hist(rankUpDown_values_tv, bins=60)
    axs[0].text(max(rankUpDown_values_tv)/2, 20, f"Number decreasing: {number_decreasing_shows}", fontsize=14)
    axs[0].text(max(rankUpDown_values_tv)/2, 35, f"Number increasing: {number_increasing_shows}", fontsize=14)
    axs[1].set_title("Most Popular Movies Movement")
    axs[1].hist(rankUpDown_values_movies, bins=60)
    axs[1].text(max(rankUpDown_values_movies) / 2, 20, f"Number decreasing: {number_decreasing_movies}", fontsize=14)
    axs[1].text(max(rankUpDown_values_movies)/2, 35, f"Number increasing: {number_increasing_movies}", fontsize=14)
    plt.show()


class DataGraphWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()


        self.overlapping_shows = self.find_overlapping_shows()
        self.overlapping_movies = self.find_overlapping_movies()

        self.display_overlapping_shows()
        self.display_overlapping_movies()

    def display_overlapping_shows(self):

        sent_str = ""
        for show in self.overlapping_shows:
            sent_str += show + ", "
        sent_str = sent_str[:-2]


        label = QLabel(self)
        label.setText("Overlapping Shows:")
        label.move(30, 50)
        id_display = QLineEdit(f"{sent_str}", self)
        id_display.move(180, 50)
        id_display.resize(700, 30)

    def display_overlapping_movies(self):

        sent_str = ""
        for movie in self.overlapping_movies:
            sent_str += movie + ", "
        sent_str = sent_str[:-2]


        label = QLabel(self)
        label.setText("Overlapping Movies:")
        label.move(30, 250)
        id_display = QLineEdit(f"{sent_str}", self)
        id_display.move(180, 250)
        id_display.resize(700, 30)

    def setup_window(self):
        self.setWindowTitle(f"Data Visualization")
        self.setGeometry(750, 100, 900, 800)

    def find_overlapping_shows(self):
        secret_key = "k_ul3l4k74"

        top_250_shows_request = requests.get(f"https://imdb-api.com/en/API/Top250TVs/{secret_key}")
        top_250_shows_json = top_250_shows_request.json()


        top_250_show_ids = []
        for show in top_250_shows_json.get('items'):
            top_250_show_ids.append(show.get('id'))

        overlapping_shows = []
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularShows""")
        popular_shows_data = cursor.fetchall()

        for show in popular_shows_data:
            if show[0] in top_250_show_ids:
                overlapping_shows.append(show[0])

        close_db(conn)

        return overlapping_shows

    def find_overlapping_movies(self):
        secret_key = "k_ul3l4k74"

        top_250_movies_request = requests.get(f"https://imdb-api.com/en/API/Top250Movies/{secret_key}")
        top_250_movies_json = top_250_movies_request.json()

        top_250_movies_ids = []
        for movie in top_250_movies_json.get('items'):
            top_250_movies_ids.append(movie.get('id'))

        overlapping_movies = []
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularMovies""")
        popular_movies_data = cursor.fetchall()

        for show in popular_movies_data:
            if show[0] in top_250_movies_ids:
                overlapping_movies.append(show[0])

        close_db(conn)

        return overlapping_movies


class RatingsWindow(QWidget):
    def __init__(self, data):
        super().__init__()


        self.data = data

        print(self.data)

        self.setup_window()

    def setup_window(self):
        self.setWindowTitle(f"Show data for show {self.data[0]}")
        self.setGeometry(750, 100, 900, 800)  # put the new window next to the original one wider than it is tall
        label = QLabel(self)
        label.setText("Show ID:")
        label.move(50, 50)
        id_display = QLineEdit(f"{self.data[0]}",self)
        id_display.move(120, 50)

        label = QLabel("Rating Percent 10:", self)
        label.move(10, 100)
        rating_percent_10 = QLineEdit(self.data[3], self)
        rating_percent_10.move(120,100)

        label = QLabel("Rating Votes 10:", self)
        label.move(230, 100)
        rating_data_10 = QLineEdit(self.data[4], self)
        rating_data_10.move(330, 100)

        label = QLabel("Rating Percent 9:", self)
        label.move(440, 100)
        rating_percent_9 = QLineEdit(self.data[5], self)
        rating_percent_9.move(540, 100)

        label = QLabel("Rating Votes 9:", self)
        label.move(650, 100)
        rating_data_9 = QLineEdit(self.data[6], self)
        rating_data_9.move(750, 100)

        label = QLabel("Rating Percent 8:", self)
        label.move(10, 200)
        rating_percent_8 = QLineEdit(self.data[7], self)
        rating_percent_8.move(120,200)

        label = QLabel("Rating Votes 8:", self)
        label.move(230, 200)
        rating_data_8 = QLineEdit(self.data[8], self)
        rating_data_8.move(330, 200)

        label = QLabel("Rating Percent 7:", self)
        label.move(440, 200)
        rating_percent_7 = QLineEdit(self.data[9], self)
        rating_percent_7.move(540, 200)

        label = QLabel("Rating Votes 7:", self)
        label.move(650, 200)
        rating_data_7 = QLineEdit(self.data[10], self)
        rating_data_7.move(750, 200)

        label = QLabel("Rating Percent 6:", self)
        label.move(10, 300)
        rating_percent_6 = QLineEdit(self.data[11], self)
        rating_percent_6.move(120,300)

        label = QLabel("Rating Votes 6:", self)
        label.move(230, 300)
        rating_data_6 = QLineEdit(self.data[12], self)
        rating_data_6.move(330, 300)

        label = QLabel("Rating Percent 5:", self)
        label.move(440, 300)
        rating_percent_5 = QLineEdit(self.data[13], self)
        rating_percent_5.move(540, 300)

        label = QLabel("Rating Votes 5:", self)
        label.move(650, 300)
        rating_data_5 = QLineEdit(self.data[14], self)
        rating_data_5.move(750, 300)

        label = QLabel("Rating Percent 4:", self)
        label.move(10, 400)
        rating_percent_4 = QLineEdit(self.data[15], self)
        rating_percent_4.move(120,400)

        label = QLabel("Rating Votes 4:", self)
        label.move(230, 400)
        rating_data_4 = QLineEdit(self.data[16], self)
        rating_data_4.move(330, 400)

        label = QLabel("Rating Percent 3:", self)
        label.move(440, 400)
        rating_percent_3 = QLineEdit(self.data[17], self)
        rating_percent_3.move(540, 400)

        label = QLabel("Rating Votes 3:", self)
        label.move(650, 400)
        rating_data_3 = QLineEdit(self.data[18], self)
        rating_data_3.move(750, 400)

        label = QLabel("Rating Percent 2:", self)
        label.move(10, 500)
        rating_percent_2 = QLineEdit(self.data[19], self)
        rating_percent_2.move(120, 500)

        label = QLabel("Rating Votes 2:", self)
        label.move(230, 500)
        rating_data_2 = QLineEdit(self.data[20], self)
        rating_data_2.move(330, 500)

        label = QLabel("Rating Percent 1:", self)
        label.move(440, 500)
        rating_percent_1 = QLineEdit(self.data[21], self)
        rating_percent_1.move(540, 500)

        label = QLabel("Rating Votes 1:", self)
        label.move(650, 500)
        rating_data_1 = QLineEdit(self.data[22], self)
        rating_data_1.move(750, 500)

        label = QLabel("Total Rating Votes:", self)
        label.move(10, 600)
        total_votes = QLineEdit(self.data[2], self)
        total_votes.move(120, 600)


class DataWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.display_list = None
        self.list_control = None
        self.ratings_window = None
        self.sort_by_rank_button = None
        self.sort_by_rankUpDown_button = None
        self.sort_by_rank_popular_movies_button = None
        self.ratings_window = None
        self.data_graph_window = None
        self.data_graph_button = None
        self.setGeometry(800, 200, 800, 500)

        self.setup_window()


    def setup_window(self):

        self.sort_by_rank_button = QPushButton("Sort by rank", self)
        self.sort_by_rank_button.move(340, 400)

        self.sort_by_rankUpDown_button = QPushButton("Sort by rankUpDown", self)
        self.sort_by_rankUpDown_button.move(100, 400)

        self.most_popular_movies_button = QPushButton("Most Popular Movies", self)
        self.most_popular_movies_button.move(400, 370)
        self.most_popular_movies_button.clicked.connect(self.change_to_popular_movies)

        self.most_popular_tv_button = QPushButton("Most Popular TV Shows", self)
        self.most_popular_tv_button.move(200, 370)
        self.most_popular_tv_button.clicked.connect(self.change_to_popular_tv_shows)

        self.top250_tv_button = QPushButton("Top 250 TV Shows", self)
        self.top250_tv_button.move(33, 370)
        self.top250_tv_button.clicked.connect(self.change_to_top250_tv_shows)

        self.data_graph_button = QPushButton("Data Visualization", self)
        self.data_graph_button.move(600, 390)
        self.data_graph_button.clicked.connect(self.open_data_graph_window)


        self.display_list = QListWidget(self)
        self.display_list.resize(650, 350)
        self.list_control = self.display_list

        self.display_tv_data()
        self.set_buttons_for_popular_tv_shows()
        # self.set_buttons_for_popular_movies()



        self.show()

    def open_data_graph_window(self):
        self.data_graph_window = DataGraphWindow()
        self.data_graph_window.show()

    def change_to_top250_tv_shows(self):
        self.set_buttons_for_top250_shows()
        self.display_top250_shows()

    def change_to_popular_tv_shows(self):
        self.set_buttons_for_popular_tv_shows()
        self.display_tv_data()

    def change_to_popular_movies(self):
        self.set_buttons_for_popular_movies()
        self.display_popular_movies()

    def display_popular_movies(self):

        self.list_control.clear()

        self.data = self.get_popular_movie_data()

        self.list_control = self.display_list

        self.put_movie_data_in_list(self.data)

        self.show()

    def set_buttons_for_top250_shows(self):
        self.sort_by_rank_button.clicked.connect(self.display_top250_shows)
        self.sort_by_rankUpDown_button.clicked.connect(self.display_top250_shows)
        self.display_list.currentItemChanged.connect(self.tv_list_item_selected)

    # def do_nothing(self):
    #     pass

    def set_buttons_for_popular_movies(self):

        self.sort_by_rank_button.clicked.connect(self.display_popular_movies)
        self.sort_by_rankUpDown_button.clicked.connect(self.display_movie_data_sorted_by_rankUpDown)
        self.display_list.currentItemChanged.connect(self.movie_list_item_selected)

    def set_buttons_for_popular_tv_shows(self):

        self.sort_by_rank_button.clicked.connect(self.display_tv_data)
        self.sort_by_rankUpDown_button.clicked.connect(self.display_tv_data_sorted_by_rankUpDown)
        self.display_list.currentItemChanged.connect(self.tv_list_item_selected)



    def display_tv_data_sorted_by_rankUpDown(self):
        self.data = self.get_popular_tv_data_sorted_by_rankUpDown()

        self.list_control = self.display_list

        self.list_control.clear()

        self.put_tv_data_in_list(self.data)

        self.show()

    def display_movie_data_sorted_by_rankUpDown(self):

        self.data = self.get_popular_movie_data_sorted_by_rankUpDown()

        self.list_control = self.display_list

        self.list_control.clear()

        self.put_tv_data_in_list(self.data)

        self.show()

    def display_top250_shows(self):
        self.list_control.clear()
        self.data = self.get_top250_tv_data()
        self.list_control = self.display_list
        self.put_tv_data_in_list(self.data)
        self.show()

    def display_tv_data(self):

        self.list_control.clear()

        self.data = self.get_popular_tv_data()

        self.list_control = self.display_list

        self.put_tv_data_in_list(self.data)

        self.show()

    def get_popular_movie_data(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularMovies""")
        data = cursor.fetchall()

        close_db(conn)

        return data

    def get_top250_tv_data(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM Top250Data""")
        data = cursor.fetchall()

        close_db(conn)

        return data

    def get_popular_tv_data(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularShows""")
        data = cursor.fetchall()

        close_db(conn)

        return data

    def get_popular_movie_data_sorted_by_rankUpDown(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularMovies ORDER BY rankUpDown DESC""")
        data = cursor.fetchall()

        close_db(conn)
        return data

    def get_popular_tv_data_sorted_by_rankUpDown(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularShows ORDER BY rankUpDown DESC""")
        data = cursor.fetchall()

        close_db(conn)

        return data

    def movie_list_item_selected(self, current:QListWidgetItem, previous:QListWidgetItem):
        print("Movie")
        print(current.data(0).split("\t")[0])

        movie_id = current.data(0).split("\t")[0]

        conn, cursor = open_db("IMDBDatabase.sqlite")
        data = cursor.execute('''SELECT * FROM
        HighestMoversMovies
        ''').fetchall()
        close_db(conn)

        entry = None
        for movie_entry in data:
            if movie_entry[0] == movie_id:
                entry = movie_entry
        if entry != None:
            self.data_window = RatingsWindow(entry)
            self.data_window.show()



    def tv_list_item_selected(self, current:QListWidgetItem, previous:QListWidgetItem):
        print("TV")
        print(current.data(0).split("\t")[0])

        show_id = current.data(0).split("\t")[0]

        conn, cursor = open_db("IMDBDatabase.sqlite")
        data = cursor.execute('''SELECT * FROM
        UserRatings
        ''').fetchall()
        close_db(conn)

        entry = None
        for show_entry in data:
            if show_entry[0] == show_id:
                entry = show_entry
        if entry != None:
            self.data_window = RatingsWindow(entry)
            self.data_window.show()





    def put_tv_data_in_list(self, data):
        for item in data:
        # for i in range(10):
            display_text = f"{item[0]}\t\t\t{item[1]}\t\t\t{item[2]}\t\t\t{item[3]}\t\t\t{item[4]}\t\t\t{item[5]}\t\t\t{item[6]}"

            list_item = QListWidgetItem(display_text, listview=self.list_control)

        self.show()

    def put_movie_data_in_list(self, data):
        for item in data:
            display_text = f"{item[0]}\t\t\t{item[1]}\t\t\t{item[2]}\t\t\t{item[3]}\t\t\t{item[4]}\t\t\t{item[5]}\t\t\t{item[6]}"

            list_item = QListWidgetItem(display_text, listview=self.list_control)

        self.show()

    def open_tv_info_window(self):
        print("Touch")

    def open_data_visualization_window(self):
        self.data_window = DataWindow(1)
        self.data_window.show()


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 800, 500)
        self.setup_window()
        self.data_window = None

    def update_data(self):
        # os.execl(sys.executable, sys.executable, *sys.argv)
        pass

    def setup_window(self):
        update_data_button = QPushButton("Update Data", self)
        update_data_button.move(200, 400)
        update_data_button.clicked.connect(self.update_data)

        data_visualization_button = QPushButton("Open Data", self)
        data_visualization_button.move(200, 200)
        data_visualization_button.clicked.connect(self.open_data_visualization_window)

        self.show()



    def open_data_visualization_window(self):
        self.data_window = DataWindow(1)
        self.data_window.show()

def main():
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = StartWindow()

    plot_data()


    sys.exit(qt_app.exec())





