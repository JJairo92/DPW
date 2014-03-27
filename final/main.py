# Jairo Jurado
# DPW
# 03/27/2014
# Music Practical

import webapp2
from page import Page

class MusicController(webapp2.RequestHandler):
	def get(self):
		page = Page()

		self.response.write(page.header + page._footer)

app = webapp2.WSGIApplication([
	('/', MusicController)
], debug=True)