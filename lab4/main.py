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

		animals = [puma, bear, wolf]

		self.response.write(page.header + page.links)
		if self.request.GET:
			animal = int(self.request.GET['animal'])

			name = animals[animal].name
			phylum = animals[animal].phylum
			classs = animals[animal].classs
			order = animals[animal].order
			family = animals[animal].family
			genus = animals[animal].genus
			img = animals[animal].img
			lifespan = animals[animal].lifespan
			habitat = animals[animal].habitat
			geolocation = animals[animal].geolocation
			sound = animals[animal].sound

			info='''<div id="info">
			<h3>{name}</h3>
				<section id="properties">
					<p class="labels"><strong>Phylum:</strong></p>
					<p class="labels"><strong>Class:</strong></p>
					<p class="labels"><strong>Order:</strong></p>
					<p class="labels"><strong>Family:</strong></p>
					<p class="labels"><strong>Genus:</strong></p>
					<p class="labels"><strong>Lifespan:</strong></p>
					<p class="labels"><strong>Habitat:</strong></p>
					<p class="labels"><strong>Geolocation:</strong></p>
					<p class="labels"><strong>Sound:</strong></p>
				</section>

				<section id="details">
					<p class="detail-info">{phylum}</p>
					<p class="detail-info">{classs}</p>
					<p class="detail-info">{order}</p>
					<p class="detail-info">{family}</p>
					<p class="detail-info">{genus}</p>
					<p class="detail-info">{lifespan}</p>
					<p class="detail-info">{habitat}</p>
					<p class="detail-info">{geolocation}</p>
					<p class="detail-info">{sound}</p>
				</section>

				<div id="img">
					<img src="{img}" title="Picture of {name}" alt="Picture of {name}" />
				</div> <!-- Closes "img" div -->
			</div>'''
			info = info.format(**locals())

			self.response.write(info)

		self.response.write(page.footer)

# Animal Abstract/Super Class
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

# Puma Subclass
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

# Bear Subclass
class Bear(Animal):
	def __init__(self):
		super(Bear, self).__init__() # instantiating function for super class
		self.name = "Bear"
		self.phylum = "Chordata"
		self.classs = "Mammalia"
		self.order = "Carnivora"
		self.family = "Ursidae"
		self.genus = "Ursus"
		self.img = "http://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Sloth_bear_stand.jpg/399px-Sloth_bear_stand.jpg"
		self.lifespan = "15 to 35 years"
		self.habitat = "Forest and Mountainous Regions"
		self.geolocation = "North America, South America, Europe, and Asia"

# Wolf Subclass
class Wolf(Animal):
	def __init__(self):
		super(Wolf, self).__init__() # instantiating function for super class
		self.name = "Wolf"
		self.phylum = "Chordata"
		self.classs = "Mammalia"
		self.order = "Carnivora"
		self.family = "Canidae"
		self.genus = "Canis"
		self.img = "http://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Canis_lupus_laying.jpg/384px-Canis_lupus_laying.jpg"
		self.lifespan = "10 to 12 years"
		self.habitat = "Grass Plains and Woodlands"
		self.geolocation = "North America, Eurasia, and North Africa"

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)