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

		form_settings = [{"song":"Like a Rolling Stone"},{"song":"Satisfaction"}]
		form = Form(form_settings)
		form.update()

		self.response.write(page.header + form.getForm + page.footer)

		# if self.request.GET['button']:
		# 	model = MusicModel(self.request.GET['button'])
		# 	view = MusicView(model.content)

		# 	self.response.write(view.content)

# class MusicModel(object):
# 	def __init__(self):
# 		self.__url = "Music.xml"
# 		self.__req = urllib2.Request(self.__url)
# 		self.__opener = urllib2.build_opener()
# 		self.send()

# 	def send(self):
# 		self.__result = self.__opener.open(self.__req)
# 		self.sort()

# 	def sort(self):
# 		self.__xmldoc = minidom.parse(self.__result)
# 		self.__do = TrackData()
# 		songs = self.__xmldoc.getElementsByTagName('track')
# 		for song in songs:
# 			songsDict = dict()
# 			title = song.getElementsByTagName('title')[0].firstChild.nodeValue
# 			artist = song.getElementsByTagName('artist')[0].firstChild.nodeValue
# 			length = song.getElementsByTagName('length')[0].firstChild.nodeValue
# 			year = song.getElementsByTagName('year')[0].firstChild.nodeValue
# 			label = song.getElementsByTagName('label')[0].firstChild.nodeValue

# 			songsDict = [title]
# 			self.__do.songs.append(songsDict)
# 		print self.__do.songs


class TrackData(object):
	def __init__(self):
		self.songs = []

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)