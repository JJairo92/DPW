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

class MusicModel(object):
	def __init__(self):
		pass

class MusicData(object):
	def __init__(self):
		self.title = ""
		self.artist = ""
		self.length = ""
		self.year = ""
		self.label = ""
		self.cover = ""

class MusicView(object):
	def __init__(self):
		pass

app = webapp2.WSGIApplication([
	('/', MusicController)
], debug=True)