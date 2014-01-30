# Jairo Jurado
# 01/29/2014
# DPW
# Final Exam - Music with XML

import webapp2
from page import *
import urllib2
from xml.dom import minidom

''' The app buttons don't link, I never understood how to do that since that was lab 4(Fox Lab)and that's the lab I struggled with the most and still did not managed to get it to work. As far as everything else, I think it would display correctly if I knew how to link the buttons. The button names, are hard coded, the instructions said not to do that but there was no other way I knew how to do it. I know since this app doesn't really work, it will be a very low grade. I guess I'd be seeing you the next time I take this class.

	As far as the extra credit, the music player, the songs do play; not the way you wanted them to be displayed but the audio does work. I hope you have a good month. See you next time.'''

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()
		page.update()

		form_settings = [{"song":"Like a Rolling Stone", "name":"button"},{"song":"Satisfaction", "name":"button"},{"song":"Imagine", "name":"button"},{"song":"What's Going On", "name":"button"},{"song":"Respect", "name":"button"},{"song":"Good Vibrations", "name":"button"},{"song":"Hey Jude", "name":"button"},{"song":"Smells Like Teen Spirit", "name":"button"},{"song":"What I'd Say", "name":"button"}]
		form = Form(form_settings)
		form.update()

		self.response.write(page.header + form.getForm + page.footer)

		if self.request.GET:
			model = MusicModel(self.request.GET['button'])
			view = MusicView(model.do)
			self.response.write(view.content)
			
class MusicModel(object):
	def __init__(self, button):
		self.__url = "Music.xml"
		self.__req = urllib2.Request(self.__url)
		self.__opener = urllib2.build_opener()

	def send(self):
		self.__result = open(self.__url, 'r')
		self.sort()

	def sort(self):
		self.__xmldoc = minidom.parse(self.__result)
		self.__do = TrackData()
		songs = self.__xmldoc.getElementsByTagName('track')
		for song in songs:
			songsDict = dict()
			title = song.getElementsByTagName('title')[0].firstChild.nodeValue
			artist = song.getElementsByTagName('artist')[0].firstChild.nodeValue
			length = song.getElementsByTagName('length')[0].firstChild.nodeValue
			year = song.getElementsByTagName('year')[0].firstChild.nodeValue
			label = song.getElementsByTagName('label')[0].firstChild.nodeValue
			cover = song.getElementsByTagName('cover')[0].firstChild.nodeValue

			songsDict = [title, artist, length, year, label, cover]
			self.__do.songs.append(songsDict)
		print self.__do.songs
		# self.__result.read()

	@property
	def do(self):
		return self.__do


class TrackData(object):
	def __init__(self):
		self.songs = []

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)