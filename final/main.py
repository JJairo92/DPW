# Jairo Jurado
# DPW
# 03/27/2014
# Music Practical

import webapp2
from page import Page
import urllib2
from xml.dom import minidom

class MusicController(webapp2.RequestHandler):
	def get(self):
		page = Page()

		self.response.write(page.header)

		self.response.write(page._footer)

class MusicModel(object):
	def __init__(self):
		self.__url = "http://rebeccacarroll.com/api/music/music.xml"
		self.__request = urllib2.Request(self.__url)
		self.__opener = urllib2.build_opener()
		self.send()

	def send(self):
		self.__result = self.__opener.open(self.__request)
		self.sort()

	# def sort(self):


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