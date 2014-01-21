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

	

