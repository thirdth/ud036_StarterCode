# Function creates a class for the movies listed in entertainment-center.py.
# The function takes inputs of Title of Movie, Storyline of Movie, Poster Image
# and the youTube address of the trailer of the movie.
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
