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
        page.update()

    	self.response.write(page.header())

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

		self._footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Animal Classes</strong></p>
		</footer>
	</html>'''

	def header(self):
		return self._header

	def footer(self):
		return self._footer

	def update(self):
		self._header = self._header.format(**locals())