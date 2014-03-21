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

app = webapp2.WSGIApplication([
	('/', VideoGame)
], debug=True)