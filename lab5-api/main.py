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
		page.update()

		self.response.write(page.header + page.footer)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)