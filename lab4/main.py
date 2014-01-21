# Jairo Jurado
# 01/15/2014
# DPW
# Lab 4 Fox

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = MainInfo()
		page.title = "Animal Classes"
		page.css = '<link rel="stylesheet" type="text/css" href="css/main.css"  />'
		page.update()

		

		animals = [puma,bear,wolf]

		self.response.write(page.header)
		self.response.write(page.nav)
		if self.request.GET:
			a = int(self.request.GET('animal'])
			self.response.write(page.body(animals[a]))
		self.response.write(page.footer)

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

		self._nav = '''
		<nav>
			<button><a href="/animal=0">Puma</a></button>
			<button><a href="/animal=1">Bear</a></button>
			<button><a href="/animal=2">Wolf</a></button>
		</nav>'''

		self._footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Animal Classes</strong></p>
		</footer>
	</html>'''

	@property
	def header(self):
		return self._header

	@property
	def nav(self):
		return self._nav

	@property
	def footer(self):
		return self._footer

	def update(self):
		self._header = self._header.format(**locals())

	

class MainInfo(PageBase):
	def __init__(self, obj):
		super(MainInfo, self).__init__()
		self._body = '''
		<h2>hello</h2>
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
			<p class='prop-info'>{obj.life}</p>
			<p class='prop-info'>{obj.habitat}</p>
			<p class='prop-info'>{obj.geo}</p>
			<p class='prop-info'>{obj.sound}</p>'''

	@property
	def body(self):
		return self._body

	@property
	def update(self):
		self._body = self._body.format(**locals())