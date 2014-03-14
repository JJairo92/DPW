# Jairo Jurado
# DPW
# 03/13/2014
# Lab 4 - Animals

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world!')

class Animal(object):
	def __init__(self):
		self.name = ''
		self.phylum = ''
		self.classs = ''
		self.order = ''
		self.family = ''
		self.genus = ''
		self.img = ''
		self.lifespan = ''
		self.habitat = ''
		self.geolocation = ''
		self.sound = ''

	@sound.setter
	def sound(self, new_sound):
		self.sound = new_sound

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)