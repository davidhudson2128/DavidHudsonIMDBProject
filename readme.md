David Hudson

Description:
This project displays IMDB rating data for 5 specific shows, and then displays the top 250 shows and their data. 
Data is output to 'output.txt'. Certain data is then placed into two newly created databases.

Run Directions:
Run main.py

Database Layout:
The top_250_shows_db contains info about a few specific shows. The information columns are the show's the id, title, full title, year, crew, imdb rating, and imdbrating count.
The user_ratings_db contains info about shows' rating, with the columns including number of votes and percent for each rating.
The imdbId field in the user_ratings_db is foreign keyed to the top_250_shows_db id field

Missing From Project:
- GitHub Secret API key not working (After creating the API_KEY environment variable in YAML I was unable to access it within python)
- The first test isn't working properly
- No second test
- All of a sudden the build is failing at the Install Dependencies step. (Might have something to do with the pip/python on my computer)