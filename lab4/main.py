# Jairo Jurado
# DPW
# 03/13/2014
# Lab 4 - Animals

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()

		# Puma
		puma = Puma()
		puma.sound = "haaoom"

		# Bear
		bear = Bear()
		bear.sound = "uuaaah"

		# Wolf
		wolf = Wolf()
		wolf.sound = "aaooo"

		self.response.write(page.header + page.links)

		self.response.write(page.footer)

# Animal Abstract Class
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

class Puma(Animal):
	def __init__(self):
		super(Puma, self).__init__() # instantiating function for super class
		self.name = "Puma"
		self.phylum = "Chordata"
		self.classs = "Mammalia"
		self.order = "Carnivora"
		self.family = "Felidae"
		self.genus = "Puma"
		self.img = "http://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/PumaNov06.jpg/517px-PumaNov06.jpg"
		self.lifespan = "10 to 15 years"
		self.habitat = "Mountain Forest and Jungle"
		self.geolocation = "North and South America"

class Bear(Animal):
	def __init__(self):
		super(Bear, self).__init__() # instantiating function for super class
		self.name = "Bear"
		self.phylum = "Chordata"
		self.classs = "Mammalia"
		self.order = "Carnivora"
		self.family = "Ursidae"
		self.genus = "Ursus"
		self.img = ""
		self.lifespan = "15 to 35 years"
		self.habitat = "Forest and Mountainous Regions"
		self.geolocation = "North America, South America, Europe, and Asia"

class Wolf(Animal):
	def __init__(self):
		super(Wolf, self).__init__() # instantiating function for super class
		self.name = "Wolf"
		self.phylum = "Chordata"
		self.classs = "Mammalia"
		self.order = "Carnivora"
		self.family = "Canidae"
		self.genus = "Canis"
		self.img = ""
		self.lifespan = "10 to 12 years"
		self.habitat = "Grass Plains and Woodlands"
		self.geolocation = "North America, Eurasia, and North Africa"


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)