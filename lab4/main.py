# Jairo Jurado
# 01/15/2014
# DPW
# Lab 4 Fox

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Nav()
		page.title = "Animal Classes"
		page.css = '<link rel="stylesheet" type="text/css" href="css/main.css"  />'
		page.method = "GET"
		page.update()

		puma = Animal()
		puma.name = "Puma"
		puma.phylum = "Chordata"
		puma.classs = "Mammalia"
		puma.order = "Carnivora"
		puma.family = "Felidae"
		puma.genus = "Puma"
		puma.lifespan = "10 to 15 years"
		puma.habitat = "Mountain Forest and Jungle"
		puma.geolocation = "North and South America"
		puma.sound = "aaoom"
		puma.update()

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
		bear.update()

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
		wolf.update()

		animals = [puma,bear,wolf]

		self.response.write(page.header)
		self.response.write(page.nav)
		if self.request.GET:
			a = int(self.request.GET['animal'])
			self.response.write(self.mainInfo(animals[a]))
		self.response.write(page.footer)

		def mainInfo(self, obj):
			body = '''
			<h2>{obj.name}</h2>
				<p class='properties'>Phylum:</p>
				<p class='properties'>Class:</p>
				<p class='properties'>Order:</p>
				<p class='properties'>Family:</p>
				<p class='properties'>Genus:</p>
				<p class='properties'>Average Lifespan:</p>
				<p class='properties'>Habitat:</p>
				<p class='properties'>Geolocation:</p>
				<p class='properties'>Sound:</p>

				<p class='prop-info'>{obj.phylum}</p>
				<p class='prop-info'>{obj.classs}</p>
				<p class='prop-info'>{obj.family}</p>
				<p class='prop-info'>{obj.genus</p>
				<p class='prop-info'>{obj.lifespan}</p>
				<p class='prop-info'>{obj.habitat}</p>
				<p class='prop-info'>{obj.geolocation}</p>
				<p class='prop-info'>{obj.sound}</p>'''
			body = body.format(**locals())
			return body

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)


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

	# @property
	def name(self):
		return self.name

	def update(self):
		self.name = self.name.format(**locals())

class PageBase(object):
	def __init__(self):
		self._header = '''<!DOCTYPE>
	<html lang="en">
		<head>
			<title>{self.title}</title>
			{self.css}
		</head>
		<body>
			<h1>Animal Classes</h1>'''

		self.__footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Animal Classes</strong></p>
		</footer>
	</html>'''

	@property
	def header(self):
		return self._header

	@property
	def footer(self):
		return self.__footer

	# def update(self):
	# 	self._header = self._header.format(**locals())

class Nav(PageBase):
	def __init__(self):
		super(Nav, self).__init__()

		self.method = ''

		self._nav = '''
		<form action="" method="{self.method}">
			<a href="/?animal=0" name="animal"><button>Puma</button></a>
			<a href="/?animal=1" name="animal"><button>Bear</button></a>
			<a href="/?animal=2" name="animal"><button>Wolf</button></a>
		</form>'''

	@property
	def nav(self):
		return self._nav
	
	def update(self):
		self._header = self._header.format(**locals())
		self._nav = self._nav.format(**locals())