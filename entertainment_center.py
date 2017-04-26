# Brings in all the relevant files associated with this program
import fresh_tomatoes
import media

# list of the movies to be shown in browser
star_wars = media.Movie(
    "Star Wars",
    "Stars battle it our for intergalactic supremacy",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BYzQ2OTk4N2QtOGQwNy00MmI3LWEwNmEtOTk0OTY3NDk2MGJkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,664,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=nywPf1p-BBY")

departed = media.Movie(
    "The Departed",
    "Boston Cops aren't sure who is good and who is bad",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=SGWvwjZ0eDc")

karate_kid = media.Movie(
    "The Karate Kid",
    "New kid comes to town, steals kid's girlfriend and then beats him up",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTkzY2YzNmYtY2ViMS00MThiLWFlYTEtOWQ1OTBiOGEwMTdhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX640_CR0,0,640,999_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=n7JhKCQnEqQ")

gravity = media.Movie(
    "Gravity",
    "Two people go to space, one returns",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=OiTiKOy59o4")

arrival = media.Movie(
    "Arrival",
    "ESL teacher in Montana learns to see the future",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SY1000_CR0,0,640,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

good_will_hunting = media.Movie(
    "Good Will Hunting",
    "Uneducated Boston man follows a girl to California",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,655,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=QSMvyuEeIyw")

# creates a variable for fresh_tomatoes file to cycle through
movies = [star_wars, departed, karate_kid, gravity, arrival, good_will_hunting]

# executes the file fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
