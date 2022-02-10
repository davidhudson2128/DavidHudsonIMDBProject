import requests
import json
# import pprint


# sample comment to test workflow
def get_top_250_shows(api_key):
    # top_250_shows_request = requests.get(f"https://imdb-api.com/en/API/Top250TVs/{api_key}")
    # top_250_shows_json = top_250_shows_request.json()

    # store data to file to avoid API requests
    # with open("top_250_shows.json", "w") as file:
    #     file.write(json.dumps(top_250_shows_json))
    # read data from file
    with open("top_250_shows.json", "r") as file:
        top_250_shows_json = json.load(file)

    return top_250_shows_json


def write_top_250_shows_data_to_file(file_name: str, shows_data):
    with open(file_name, "a") as output:
        output.write("********** Top 250 Shows **********\n"
                     "***********************************\n\n")

        for show in shows_data.get('items'):
            output.write(f"Show #{show.get('rank')}: {show.get('fullTitle')}\n"
                         f"\t Crew: {show.get('crew')}\n"
                         f"\t IMDB Rating: {show.get('crew')}\n"
                         f"\t IMDB Rating Count: {show.get('imDbRatingCount')}\n"
                         f"\t JSON data: {show}\n\n")


def write_user_ratings_data_to_file(file_name: str, shows_data, imdb_api_key):
    print(shows_data)
    show_1_id = shows_data.get('items')[0].get('id')
    show_50_id = shows_data.get('items')[49].get('id')
    show_100_id = shows_data.get('items')[99].get('id')
    show_200_id = shows_data.get('items')[199].get('id')

    # wheel_of_time_request = requests.get(f'https://imdb-api.com/en/API/SearchTitle/{imdb_api_key}/wheel of time')
    # show_wheel_of_time_id = wheel_of_time_request.json().get('results')[0].get('id')
    show_wheel_of_time_id = 'tt0331080'

    # ratings_data_show_1 = requests.get(f"https://imdb-api.com/en/API/UserRatings/{imdb_api_key}/{show_1_id}").json()
    # ratings_data_show_50 = requests.get(f"https://imdb-api.com/en/API/UserRatings/{imdb_api_key}/{show_50_id}").json()
    # ratings_data_show_100 = requests.get(f"https://imdb-api.com/en/API/UserRatings/{imdb_api_key}/{show_100_id}").json()
    # ratings_data_show_200 = requests.get(f"https://imdb-api.com/en/API/UserRatings/{imdb_api_key}/{show_200_id}").json()
    # ratings_data_show_wheel_of_time = requests.get(
    #     f"https://imdb-api.com/en/API/UserRatings/{api_key}/{show_wheel_of_time_id}").json()

    with open("ratings_data_show_1.json", "r") as file:
        ratings_data_show_1 = json.load(file)
    with open("ratings_data_show_50.json", "r") as file:
        ratings_data_show_50 = json.load(file)
    with open("ratings_data_show_100.json", "r") as file:
        ratings_data_show_100 = json.load(file)
    with open("ratings_data_show_200.json", "r") as file:
        ratings_data_show_200 = json.load(file)
    with open("ratings_data_wheel_of_time.json", "r") as file:
        ratings_data_show_wheel_of_time = json.load(file)

    # Writing to file
    with open(file_name, "w") as output:

        output.write("********** Ratings Data For Shows 1, 50, 100, 200, Wheel of Time **********\n"
                     "***************************************************************************\n\n")

        # Show 1
        output.write(f"Show 1 Ratings Data:\n"
                     f"\t Name: {ratings_data_show_1.get('title')}\n")
        for rating in ratings_data_show_1.get('ratings'):
            output.write(
                f"\t Rating of {rating.get('rating')}: {rating.get('percent')} ({rating.get('votes')} votes)\n")
        output.write(f"\t JSON data: {ratings_data_show_1}\n\n")

        # Show 50
        output.write(f"Show 50 Ratings Data:\n"
                     f"\t Name: {ratings_data_show_50.get('title')}\n")
        for rating in ratings_data_show_50.get('ratings'):
            output.write(
                f"\t Rating of {rating.get('rating')}: {rating.get('percent')} ({rating.get('votes')} votes)\n")
        output.write(f"\t JSON data: {ratings_data_show_50}\n\n")

        # Show 100
        output.write(f"Show 100 Ratings Data:\n"
                     f"\t Name: {ratings_data_show_100.get('title')}\n")
        for rating in ratings_data_show_100.get('ratings'):
            output.write(
                f"\t Rating of {rating.get('rating')}: {rating.get('percent')} ({rating.get('votes')} votes)\n")
        output.write(f"\t JSON data: {ratings_data_show_100}\n\n")

        # Show 200
        output.write(f"Show 200 Ratings Data:\n"
                     f"\t Name: {ratings_data_show_200.get('title')}\n")
        for rating in ratings_data_show_200.get('ratings'):
            output.write(
                f"\t Rating of {rating.get('rating')}: {rating.get('percent')} ({rating.get('votes')} votes)\n")
        output.write(f"\t JSON data: {ratings_data_show_200}\n\n")

        # Show Wheel Of Time
        output.write(f"Show Wheel of Time Data:\n"
                     f"\t Name: {ratings_data_show_wheel_of_time.get('title')}\n")
        for rating in ratings_data_show_wheel_of_time.get('ratings'):
            output.write(
                f"\t Rating of {rating.get('rating')}: {rating.get('percent')} ({rating.get('votes')} votes)\n")
        output.write(f"\t JSON data: {ratings_data_show_wheel_of_time}\n\n")

        output.write("\n\n")


if __name__ == '__main__':

    with open("secret_api_key.txt", "r") as secret_file:
        api_key = secret_file.read()

    top_250_shows_data = get_top_250_shows(api_key)
    output_file = "output.txt"

    write_user_ratings_data_to_file(output_file, top_250_shows_data, api_key)
    write_top_250_shows_data_to_file(output_file, top_250_shows_data)
