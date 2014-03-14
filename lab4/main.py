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

		print puma.name

		# Bear
		bear = Animal()
		bear.name = "Bear"
		bear.phylum = "Chordata"
		bear.classs = "Mammalia"
		bear.order = "Carnivora"
		bear.family = "Ursidae"
		bear.genus = "Ursus"
		bear.lifespan = "15 to 35 years"
		bear.habitat = "Forest and Mountainous Regions"
		bear.geolocation = "North America, South America, Europe, and Asia"
		bear.sound = "uuaaah"

		# Wolf
		wolf = Animal()
		wolf.name = "Wolf"
		wolf.phylum = "Chordata"
		wolf.classs = "Mammalia"
		wolf.order = "Carnivora"
		wolf.family = "Canidae"
		wolf.genus = "Canis"
		wolf.lifespan = "10 to 12 years"
		wolf.habitat = "Grass Plains and Woodlands"
		wolf.geolocation = "North America, Eurasia, and North Africa"
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
		super(Animal, self).__init__() # instantiating function for super class
		self.name = "Puma"
		self.phylum = "Chordata"
		self.classs = "Mammalia"
		self.order = "Carnivora"
		self.family = "Felidae"
		self.genus = "Puma"
		self.lifespan = "10 to 15 years"
		self.habitat = "Mountain Forest and Jungle"
		self.geolocation = "North and South America"


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)