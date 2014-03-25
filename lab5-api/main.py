# Jairo Jurado
# DPW
# 03/18/2014
# Lab 5 - Bands in Town API

import webapp2
from page import Page
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page() # variable to hold "Page" class form page.py

		self.response.write(page.header + page.form)

		if self.request.GET:
			# API things
			artist = self.request.GET['artist']
			artist = artist.replace(" ","%20")
			url = "http://api.bandsintown.com/artists/"+artist+"/events?format=xml&api_version=2.0&app_id=artistElookup"

			request = urllib2.Request(url) # assemble request
			opener = urllib2.build_opener() # use urllib2 to create an object to get the url
			result = opener.open(request) # use url to get a result - request info from api

			xmldoc = minidom.parse(result) # parses the result

			self.response.write("<h2>"+xmldoc.getElementsByTagName('name')[0].firstChild.nodeValue+"</h2>")
			self.response.write("<img src='"+xmldoc.getElementsByTagName('image_url')[0].firstChild.nodeValue+"' />")
			content = ""
			events = xmldoc.getElementsByTagName('event')

			for event in events:
				content += "<h3>"+event.getElementsByTagName('title')[0].firstChild.nodeValue+"</h3>"
				content += "<h4>"+event.getElementsByTagName('formatted_datetime')[0].firstChild.nodeValue+"</h4>"
				content += "<h4>"+event.getElementsByTagName('formatted_location')[0].firstChild.nodeValue+"</h4>"
				content += "<h4>"+event.getElementsByTagName('ticket_status')[0].firstChild.nodeValue+"</h4>"
				try:
					content += "<a href='"+event.getElementsByTagName('ticket_url')[0].firstChild.nodeValue+"' target='_blank'>Buy Tickets</a>"
				except:
					pass
				content += "<br />"

			self.response.write(content)

		self.response.write(page.footer)


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)