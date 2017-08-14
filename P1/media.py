import webbrowser

class Movie(object):
	"""docstring for Movie"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,realease_date):
		self.title = movie_title
		storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url=trailer_youtube
		self.movie_release_date=realease_date


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


		