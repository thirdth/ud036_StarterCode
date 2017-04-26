# creates class for the movies in entertainment_center.py to go into so you DRY
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
