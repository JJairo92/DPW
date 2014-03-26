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
		'''This class'''
		page = Page() # variable to hold "Page" class form page.py

		self.response.write(page.header + page.form) # writes header and search box to page

		if self.request.GET:
			# sets a variable to the user input
			artist = self.request.GET['artist']
			artist = artist.replace(" ","%20")

			am = ArtistModel(artist) # calls ArtistModel Class and assigns it to "am"
			av = ArtistView(am.data) # calls ArtistView Class and assigns it to "av"

			self.response.write(av.content) # prints the content acquired from api

		self.response.write(page.footer) # writes footer to page

class ArtistModel(object):
	'''This class grabs the search input, and organizes it by using the ArtistData class'''
	def __init__(self, artist):
		# url from where the information will be requested
		self.__url = "http://api.bandsintown.com/artists/"+artist+"/events?format=xml&api_version=2.0&app_id=artistElookup"

		# assemble request
		self.__request = urllib2.Request(self.__url)
		# use urllib2 to create an object to get the url
		self.__opener = urllib2.build_opener()
		self.send() # calls the send function

	def send(self):
		# use url to get a result - request info from api
		self.__result = self.__opener.open(self.__request)
		self.sort() # calls the sort function

	def sort(self):
		# parses the result
		self.__xmldoc = minidom.parse(self.__result)
		self.__data = ArtistData() # variable to hold the information being requested
		self.__data.name = self.__xmldoc.getElementsByTagName('name')[0].firstChild.nodeValue # variable to hold the artist's name
		self.__data.img = self.__xmldoc.getElementsByTagName('image_url')[0].firstChild.nodeValue # variable to hold the image url

		events = self.__xmldoc.getElementsByTagName('event') # xml tag where everything inside will be looped through

		# loops through each "event" xml tag
		for event in events:
			event_dict = dict() # dictionary to hold all 5 variables "event_name, event_date, event_location, event_ticket_status, and event_ticket_url"

			# assigns each tag acquired to a variable so that it can be appended to the event_dict dictionary
			event_name = event.getElementsByTagName('title')[0].firstChild.nodeValue
			event_date = event.getElementsByTagName('formatted_datetime')[0].firstChild.nodeValue
			event_location = event.getElementsByTagName('formatted_location')[0].firstChild.nodeValue
			event_ticket_status = event.getElementsByTagName('ticket_status')[0].firstChild.nodeValue

			# checks to see if there is something inside the "ticket_url" tag; if there is, it will be added to the event_dict dictionary
			try:
				event_ticket_url = event.getElementsByTagName('ticket_url')[0].firstChild.nodeValue
			except:
				pass

			# array to hold each variable
			event_dict = [event_name, event_date, event_location, event_ticket_status, event_ticket_url]

			self.__data.events.append(event_dict) # event_dict is added to the events attribute in the ArtistData class

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
	'''This class displays all the information on the page'''
	def __init__(self, data):
		self.__content = "<div id='name-picture'><h2>"+data.name+" Concerts</h2>" # Artist name
		self.__content += "<img src='"+data.img+"' title='Image of artist "+data.name+"'' alt='Image of artist "+data.name+"'' /></div>" # Image of artist

		# loops through the events array in ArtistData class so all the information can be displayed
		for event in data.events:
			self.__content += "<div id='events'><div class='event'><h3>"+event[0]+"</h3>"
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

			self.__content += "</div><!-- Closes 'event' div --></div><!-- Closes 'events' div -->"

	@property
	def content(self):
		return self.__content

app = webapp2.WSGIApplication([
	('/', ArtistController)
], debug=True)