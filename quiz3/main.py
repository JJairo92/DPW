# Jairo Jurado
# DPW
# 03/20/2014
# Quiz 3

import webapp2

# Abstract Class
class VideoGame(webapp2.RequestHandler):
	def get(self):
		self._name = "Name"
		self._genre = "Genre"

	@property
	def name(self):
		return self._name

	@property
	def genre(self):
		return self._genre

# Subclass 1
class Kill(VideoGame):
	def __init__(self):
		super(Kill, self).__init__()
		self._name = "Kill to Live"
		self._genre = "Third Person Shooter"
		self._developer = "Unshaken Studios"
		self._publisher = "Life+Death"

app = webapp2.WSGIApplication([
	('/', VideoGame)
], debug=True)