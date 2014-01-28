# Jairo Jurado
# 01/22/2014
# DPW
# Lab 5 API - League of Legends

import webapp2
from page import *
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
	def get(self):
		if self.request.GET:
			artist = self.request.GET['artist']
			xmldoc = minidom.parse(result)
		page = Page()
		# form_settings =
		page.update()

		self.response.write(page.header + page.footer)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)

class Model(object):
	def __init__(self, artist):
		self.__url = "http://api.bandsintown.com/artists/"+artist+".json?app_id=artistElookup"
		self.__req = urllib2.Request(self.__url)
		self.__opener = urllib2.build_opener()
		self.__result = self.__opener.open(self.__req)
		self.__obj = json.load(self.__result)
