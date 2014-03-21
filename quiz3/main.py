# Jairo Jurado
# DPW
# 03/20/2014
# Quiz 3

import webapp2

# Abstract Class
class VideoGame(webapp2.RequestHandler):
	def get(self):
		self._name = ""
		self._genre = ""
		self._developer = ""
		self._publisher = ""

	@property
	def name(self):
		return self._name

	@property
	def genre(self):
		return self._genre

app = webapp2.WSGIApplication([
	('/', VideoGame)
], debug=True)