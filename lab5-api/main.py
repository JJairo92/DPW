# Jairo Jurado
# 01/22/2014
# DPW
# Lab 5 API - League of Legends

import webapp2
from page import *

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world!')
		#a570c3ba-1ee0-48d1-9311-8271b2c00bab (key for API)
		page = Page()
		page.update()

		self.response.write(page.header + page.footer)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)