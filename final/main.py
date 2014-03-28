# Jairo Jurado
# DPW
# 03/27/2014
# Music Practical

import webapp2
from page import Page
import urllib2
from xml.dom import minidom

class MusicController(webapp2.RequestHandler):
	'''This is the main controller for this music app'''
	def get(self):
		page = Page() # variable to hold Page class in page.py
		mm = MusicModel() # variable to hold MusicModel class
		mv = MusicView(mm.data) # variable to hold MusicView class

		self.response.write(page.header + mv.buttons) # writes header and buttons to page

		if self.request.GET:
			'''I did not know what other way to do it so I'm displaying the information through the controller and not the view. I do know how to use a View Class as you'll be able to see with the buttons I created by using the MusicView Class. However, for this particular case I did not know how to display each individual album's information'''
			song = int(self.request.GET['song'])

			title = mm.data.songs[song][0]
			artist = mm.data.songs[song][1]
			length = mm.data.songs[song][2]
			year = mm.data.songs[song][3]
			label = mm.data.songs[song][4]
			cover = mm.data.songs[song][5]

			info = '''<h2>{title}</h2>
			<img src="{cover}" />
			<p><strong>Artist: </strong>{artist}</p>
			<p><strong>Length: </strong>{length}</p>
			<p><strong>Year: </strong>{year}</p>
			<p><strong>Label: </strong>{label}</p>'''
			info = info.format(**locals())
			self.response.write(info)

		self.response.write(page._footer)

class MusicModel(object):
	'''This class organizes the xml data and uses the MusicData class to put it in the songs array'''
	def __init__(self):
		self.__url = "http://rebeccacarroll.com/api/music/music.xml" # url where the information is being acquired from
		self.__request = urllib2.Request(self.__url) # assembles request
		self.__opener = urllib2.build_opener() # urllib2 creates an object to get the url
		self.send() # calls send function

	def send(self):
		self.__result = self.__opener.open(self.__request)
		self.sort() # calls sort function

	def sort(self):
		self.__xmldoc = minidom.parse(self.__result) # parses the result
		self.__data = MusicData()

		songs = self.__xmldoc.getElementsByTagName('track') # xml tag where all the information will be looped from

		# loops through the songs tag
		for song in songs:
			song_dict = dict() # dictionary where all the information will be placed

			# assigns a variable to each tag
			titles = song.getElementsByTagName('title')[0].firstChild.nodeValue
			artists = song.getElementsByTagName('artist')[0].firstChild.nodeValue
			lengths = song.getElementsByTagName('length')[0].firstChild.nodeValue
			years = song.getElementsByTagName('year')[0].firstChild.nodeValue
			labels = song.getElementsByTagName('label')[0].firstChild.nodeValue
			covers = song.getElementsByTagName('cover')[0].firstChild.nodeValue

			song_dict = [titles, artists, lengths, years, labels, covers] # each variable is placed in the dictionary

			self.__data.songs.append(song_dict) # dictionary is appended to the songs array in MusicData

	@property
	def data(self):
		return self.__data # returns data object with all the info

class MusicData(object):
	'''This class holds the xml data that was acquired from the url'''
	def __init__(self):
		self.songs = [] # array where everything is placed

class MusicView(object):
	'''This class displays everything to the user; except for the information acquired from the xml data. The buttons are displayed by using this class'''
	def __init__(self, data):
		self.__buttons = ""
		print data.songs[0][0]

		num = 0 # number to be used for the links

		# adds each button to the "self.__buttons" attribute
		for song in data.songs:
			self.__buttons += "<a href='?song="+str(num)+"'><button>"+song[0]+"</button></a>"
			num += 1

	@property
	def buttons(self):
		return self.__buttons # returns the buttons so they can be called through the MusicController

app = webapp2.WSGIApplication([
	('/', MusicController)
], debug=True)