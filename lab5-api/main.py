# Jairo Jurado
# 01/22/2014
# DPW
# Lab 5 API - League of Legends

import webapp2
from page import *
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
	def get(self):
		# variable page is Page class in page.py
		page = Page()
		# form_settings from Form class in page.py
		form_settings = [{"type":"text", "label":"Enter artist name", "name":"artist"},{"type":"submit", "label":"Get Events!", "name":"submit"}]
		form = Form(form_settings)
		form.update()

		#writes all the information to the screen
		self.response.write(form.header + form.getForm + form.footer)

		# looks for user's input (the artist the user types)
		if self.request.GET:
			#assigns user's input as ArtistModel parameter
			aModel = ArtistModel(self.request.GET['artist'])
			aView = ArtistView(aModel.do)
			# writes content from ArtistView to the page
			self.response.write(aView.content)

class ArtistModel(object):
	#Setup
	def __init__(self, artist):
		# URL where api will be retrieved from
		self.__url = "http://api.bandsintown.com/artists/"+artist+"/events?format=xml&app_id=artistElookup"
		# URL request sent
		self.__req = urllib2.Request(self.__url)
		# Creates the framework to get the URL
		self.__opener = urllib2.build_opener()
		# calls send function/method
		self.send()

	#Send
	def send(self):
		#gets url and puts result in "self.__result"
		self.__result = self.__opener.open(self.__req)
		# calls sort function/method
		self.sort()

	#Sort
	def sort(self):
		#parse through string to get XML object
		self.__xmldoc = minidom.parse(self.__result)
		# assigns ArtistData abstract class to "self.__do"
		self.__do = ArtistData()
		# assigns value inside XML tag "name"(artist) to "self.__do.artist"
		self.__do.artist = self.__xmldoc.getElementsByTagName('name')[0].firstChild.nodeValue
		# variable to hold XML "venue" tags
		events = self.__xmldoc.getElementsByTagName('venue')
		# loops through each "venue" tag
		for event in events:
			eventDict = dict() # dictionary to hold all 4 variables "name, city, region, country"

			# assigns each tag to a name variable, since it's looping through each venue tag, it grabs all of them
			name = event.getElementsByTagName('name')[0].firstChild.nodeValue
			city = event.getElementsByTagName('city')[0].firstChild.nodeValue
			region = event.getElementsByTagName('region')[0].firstChild.nodeValue
			country = event.getElementsByTagName('country')[0].firstChild.nodeValue

			# dictionary to hold each variable
			eventDict = [name, city, region, country]
			# adds dictionary to events array in ArtistData class
			self.__do.events.append(eventDict)

		# variable to hold XML "event" tag info
		datesLinks = self.__xmldoc.getElementsByTagName('event')
		# loops through each "event" tag
		for el in datesLinks:
			datesLinksDict = dict() # dictionary to hold 2 variables "date, link"

			# assigns each tag variables
			date = el.getElementsByTagName('datetime')[0].firstChild.nodeValue
			link = el.getElementsByTagName('ticket_url')[0].firstChild.nodeValue

			# dictionary to hold each variable created
			datesLinksDict = [date, link]
			# adds dictionary to datesLinks array in ArtistData class
			self.__do.datesLinks.append(datesLinksDict)

	@property
	def do(self):
		return self.__do

# Abstract class
class ArtistData(object):
	def __init__(self):
		self.artist = ''
		self.events = []
		self.datesLinks = []

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)