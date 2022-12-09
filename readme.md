David Hudson

Description:
This project displays IMDB rating data for 5 specific shows, and then displays the top 250 shows and their data. 
Data is output to 'output.txt'. Certain data is then placed into two newly created databases. Data is then placed
into a gui for viewing. 'gui_test.pdf' is a manual test plan (with pictures) to explain what should happen when the graphical elements are invoked

Run Directions:
Run main.py

Database Layout:
The top_250_shows_db contains info about a few specific shows. The information columns are the show's the id, title, full title, year, crew, imdb rating, and imdbrating count.
The user_ratings_db contains info about shows' rating, with the columns including number of votes and percent for each rating.
The imdbId field in the user_ratings_db is foreign keyed to the top_250_shows_db id field
