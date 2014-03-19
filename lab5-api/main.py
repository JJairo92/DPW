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

		# API things

		self.response.write(page.header + page.form + page.footer)

		if self.request.GET:
			self.response.write("Hello")
			

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)