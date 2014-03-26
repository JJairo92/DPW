# Jairo Jurado
# DPW
# 03/18/2014
# Lab 5 - Bands in Town API

import webapp2
from page import Page
import urllib2
from xml.dom import minidom

class ArtistController(webapp2.RequestHandler):
	def get(self):
		page = Page() # variable to hold "Page" class form page.py

		self.response.write(page.header + page.form)

		if self.request.GET:
			# API things
			artist = self.request.GET['artist']
			artist = artist.replace(" ","%20")

			am = ArtistModel(artist) # calls ArtistModel Class and assigns it to "am"
			av = ArtistView(am.data) # calls ArtistView Class and assigns it to "av"

			self.response.write(av.content)

		self.response.write(page.footer)

class ArtistModel(object):
	def __init__(self, artist):
		self.__url = "http://api.bandsintown.com/artists/"+artist+"/events?format=xml&api_version=2.0&app_id=artistElookup"

		# assemble request
		self.__request = urllib2.Request(self.__url)
		# use urllib2 to create an object to get the url
		self.__opener = urllib2.build_opener()
		self.send()

	def send(self):
		# use url to get a result - request info from api
		self.__result = self.__opener.open(self.__request)
		self.sort()

	def sort(self):
		# parses the result
		self.__xmldoc = minidom.parse(self.__result)
		self.__data = ArtistData()
		self.__data.name = self.__xmldoc.getElementsByTagName('name')[0].firstChild.nodeValue
		self.__data.img = self.__xmldoc.getElementsByTagName('image_url')[0].firstChild.nodeValue

		events = self.__xmldoc.getElementsByTagName('event')

		for event in events:
			event_dict = dict()

			event_name = event.getElementsByTagName('title')[0].firstChild.nodeValue
			event_date = event.getElementsByTagName('formatted_datetime')[0].firstChild.nodeValue
			event_location = event.getElementsByTagName('formatted_location')[0].firstChild.nodeValue
			event_ticket_status = event.getElementsByTagName('ticket_status')[0].firstChild.nodeValue
			try:
				event_ticket_url = event.getElementsByTagName('ticket_url')[0].firstChild.nodeValue
			except:
				pass

			event_dict = [event_name, event_date, event_location, event_ticket_status, event_ticket_url]

			self.__data.events.append(event_dict)

	@property
	def data(self):
		return self.__data # returns data object with all the info

class ArtistData(object):
	def __init__(self):
		'''This class holds the artist data taken from the api'''
		self.name = ""
		self.img = ""
		self.events = []

class ArtistView(object):
	def __init__(self, data):
		self.__content = "<h2>"+data.name+" Concerts</h2>"
		self.__content += "<img src='"+data.img+"' title='Image of artist "+data.name+"'' alt='Image of artist "+data.name+"'' />"

		for event in data.events:
			self.__content += "<div class='event'><h3>"+event[0]+"</h3>"
			self.__content += "<div class='dates'><h4>City</h4>"
			self.__content += "<p>"+event[1]+"</p></div><!-- Closes 'dates' div -->"
			self.__content += "<div class='locations'><h4>Location</h4>"
			self.__content += "<p>"+event[2]+"</p></div><!-- Closes 'locations' div -->"
			self.__content += "<div class='statuses'><h4>Ticket Availability</h4>"
			self.__content += "<p>"+event[3]+"</p></div><!-- Closes 'statuses' div-->"
			try:
				self.__content += "<a href='"+event[4]+"' target='_blank'>Buy Tickets</a>"
			except:
				pass

			self.__content += "</div><!-- Closes 'event' div -->"

	@property
	def content(self):
		return self.__content

app = webapp2.WSGIApplication([
	('/', ArtistController)
], debug=True)