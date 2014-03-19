# Jairo Jurado
# DPW
# 03/18/2014
# Lab 5 - API Bands in Town

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world!')

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)