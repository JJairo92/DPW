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

		am = MusicModel()
		# av = MusicView()

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

	def sort(self):
		self.__xmldoc = minidom.parse(self.__result)
		self.__data = MusicData()

		songs = self.__xmldoc.getElementsByTagName('track')

		for song in songs:
			song_dict = dict()

			titles = song.getElementsByTagName('title')[0].firstChild.nodeValue

			song_dict[titles]

			self.__data.songs.append(song_dict)

	@property
	def data(self):
		return self.__data

class MusicView(object):
	def __init__(self):
		pass

class MusicData(object):
	def __init__(self):
		self.songs = []

app = webapp2.WSGIApplication([
	('/', MusicController)
], debug=True)