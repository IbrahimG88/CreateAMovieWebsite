

import webbrowser

"""In this file webbrowser built in python is imported to open the urls of the movies's trailers and image."""

class Movie():
    def __init__(self, movie_title, metascore_movie, movie_storyline, movie_casting_stars,
                movie_duration, movie_release_year, poster_image_movie, trailer_youtube_movie):

        self.title = movie_title
        self.metascore = metascore_movie
        self.storyline = movie_storyline
        self.casting_stars = movie_casting_stars
        self.duration = movie_duration
        self.release_year = movie_release_year
        self.poster_image_url = poster_image_movie
        self.trailer_youtube_url = trailer_youtube_movie

    def show_detail(self):
        webbrowser.open(self.trailer_url)
        webbrowser.open(self.poster_image_url)

"""The class Movie contains two procedures: __init__ and show_detail which has 9 arguments
including the self argument which is the Movie class instance and the 8 other arguments are instance variables.""" 
