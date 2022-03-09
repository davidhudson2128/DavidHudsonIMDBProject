import sqlite3

import PySide6.QtWidgets
from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox, QLabel, QLineEdit, QTextEdit
import sys
import numbers
from typing import Tuple



def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor

class RatingsWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setGeometry(750, 100, 900, 200)
        self.setWindowTitle("Change in Income over time")
        self.setGeometry(750, 100, 900, 200)  # put the new window next to the original one wider than it is tall
        label = QLabel(self)
        label.setText("State:")
        label.move(50, 50)
        state_display = QLineEdit("data1",self)
        state_display.move(120, 50)
        label = QLabel("2018 Income:", self)
        label.move(50, 100)
        income2018 = QLineEdit("data2", self)
        income2018.move(120,100)
        label = QLabel("2017 Income:", self)
        label.move(250, 100)
        income2017 = QLineEdit("data3",self)
        income2017.move(330,100)
        label = QLabel("2016 Income:", self)
        label.move(460, 100)
        income2017 = QLineEdit("data4", self)
        income2017.move(540, 100)
        label = QLabel("2015 Income:", self)
        label.move(670, 100)
        income2017 = QLineEdit("data5", self)
        income2017.move(750, 100)


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

        self.display_list = QListWidget(self)
        self.display_list.resize(650, 350)
        self.list_control = self.display_list

        self.display_tv_data()
        self.set_buttons_for_popular_tv_shows()
        # self.set_buttons_for_popular_movies()



        self.show()

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

        return data

    def get_top250_tv_data(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM Top250Data""")
        data = cursor.fetchall()

        return data

    def get_popular_tv_data(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularShows""")
        data = cursor.fetchall()

        return data

    def get_popular_movie_data_sorted_by_rankUpDown(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularMovies ORDER BY rankUpDown DESC""")
        data = cursor.fetchall()

        return data

    def get_popular_tv_data_sorted_by_rankUpDown(self):
        conn, cursor = open_db("IMDBDatabase.sqlite")
        cursor.execute("""SELECT * FROM MostPopularShows ORDER BY rankUpDown DESC""")
        data = cursor.fetchall()

        return data

    def movie_list_item_selected(self):
        print("TEST")

    def tv_list_item_selected(self, current:QListWidgetItem, previous:QListWidgetItem):
        #print(current.data(0).split("\t")[0])
        pass

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

    def setup_window(self):
        update_data_button = QPushButton("Push me for Demo", self)
        update_data_button.move(200, 400)
        update_data_button.clicked.connect(self.update_data)

        data_visualization_button = QPushButton("Push me for Demo", self)
        data_visualization_button.move(200, 200)
        data_visualization_button.clicked.connect(self.open_data_visualization_window)

        self.show()

    def update_data(self):
        print("Touch")

    def open_data_visualization_window(self):
        self.data_window = DataWindow(1)
        self.data_window.show()


qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
my_window = StartWindow()
sys.exit(qt_app.exec())



