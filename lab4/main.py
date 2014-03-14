# Jairo Jurado
# DPW
# 03/13/2014
# Lab 4 - Animals

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		# Puma
		self.puma = Animal()
		self.puma.name = "Puma"
		self.puma.phylum = "Chordata"
		self.puma.classs = "Mammalia"
		self.puma.order = "Carnivora"
		self.puma.family = "Felidae"
		self.puma.genus = "Puma"
		self.puma.lifespan = "10 to 15 years"
		self.puma.habitat = "Mountain Forest and Jungle"
		self.puma.geolocation = "North and South America"
		self.puma.sound = "haaoom"

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
		self.__sound = ''

	@property
	def sound(self):
		return self.__sound

	@sound.setter
	def sound(self, new_sound):
		self.__sound = new_sound

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)