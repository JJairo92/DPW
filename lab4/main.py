# Jairo Jurado
# 01/15/2014
# DPW
# Lab 4 Fox

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = PageBase()
        page.title = "Animal Classes"
        page.css = '<link rel="stylesheet" type="text/css" href="css/main.css"  />'
        page.name = "Puma"
        page.update()

        # animals = [puma,bear,wolf,lion,deer]

    	self.response.write(page.header())
    	self.response.write(page.nav())
    	self.response.write(page.body())
    	self.response.write(page.footer())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

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

		self._nav = '''<nav>
			<button><a href="">Puma</a></button>
			<button><a href="">Bear</a></button>
			<button><a href="">Wolf</a></button>
			<button><a href="">Lion</a></button>
			<button><a href="">Deer</a></button>
		</nav>'''

		self._body = ''''''

		self._footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Animal Classes</strong></p>
		</footer>
	</html>'''

	def header(self):
		return self._header

	def nav(self):
		return self._nav

	def body(self):
		return self._body

	def footer(self):
		return self._footer

	def update(self):
		self._header = self._header.format(**locals())
		self._body = self._body.format(**locals())

# class 