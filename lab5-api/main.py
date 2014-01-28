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
		page = Page()
		form_settings = [{"type":"text", "label":"Enter artist name", "name":"artist"},{"type":"submit", "label":"Get Events!", "name":"submit"}]
		form = Form(form_settings)
		form.update()

		self.response.write(form.header + form.getForm + form.footer)

		if self.request.GET:
			aModel = ArtistModel(self.request.GET['artist'])
			aView = ArtistView(aModel.getArtist)
			self.response.write(aView.content)

class ArtistModel(object):
	def __init__(self, artist):
		self.__url = "http://api.bandsintown.com/artists/"+artist+"?format=xml&app_id=artistElookup"
		self.__req = urllib2.Request(self.__url)
		self.__opener = urllib2.build_opener()
		self.__result = self.__opener.open(self.__req)
		self.__obj = json.load(self.__result)

	@property
	def getArtist(self):
		return self.__obj

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)