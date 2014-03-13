# Jairo Jurado
# DPW
# 03/13/2014
# Lab 3 - Encapsulated Calculator

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world!')

class Game(object):
	def __init__(self):
		pass

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)