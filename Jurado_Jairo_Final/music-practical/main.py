# Jairo Jurado
# 01/29/2014
# DPW
# Final Exam - Music with XML

import webapp2
from page import *
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()
		page.update()
		self.response.write(page.header + page.footer)

class MusicModel(object):
	def __init__(self):
		self.__url = "Music.xml"
		self.__req = urllib2.Request(self.__url)
		self.__opener = urllib2.build_opener()
		self.send()

	def send(self):
		self.__result = self.__opener.open(self.__req)
		self.sort()

	def sort(self):
		self.__xmldoc = minidom.parse(self.__result)
		


class TrackData(object):
	def __init__(self):
		self.name = ''
		self.artist = ''
		self.length = ''
		self.year = ''
		self.label = ''

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)