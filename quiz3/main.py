# Jairo Jurado
# 01/22/2014
# DPW
# Quiz 3

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Game1()
		info = Game2()
		page.update()
		info.update()

		self.response.write(page.header + page.info1 + info.info2 + page.footer)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)

class Page(object):
	def __init__(self):
		self.title = "YO YO"
		self.paragraph = "This is the paragraph of quiz 3. This is quiz 3!"
		self._header = '''<!DOCTYPE html>
		<html>
			<head>
				<title>{self.title}</title>
			</head>
			<body>
				<h1>Quiz 3</h1>
				<h2>Games</h2>
				<p>{self.paragraph}</p>
				'''

		self.__footer = '''
			</body>
			<footer>
				<p>Copyright &copy; 2014 <strong>Quiz 3</strong></p>
			</footer>
		</html>'''

	@property
	def header(self):
		return self._header

	@property
	def footer(self):
		return self.__footer


class Game1(Page):
	def __init__(self):
		super(Game1, self).__init__()
		self.title = "Quiz 3"
		self.game1 = "Remember to Forget"
		self.game1Genre = "Action/Adventure"

		self._info1 = '''
		<p>Game Name: {self.game1}</p>
		<p>Game Name: {self.game1Genre}</p>'''

	@property
	def info1(self):
		return self._info1

	def update(self):
		self._header = self._header.format(**locals())
		self._info1 = self._info1.format(**locals())

class Game2(Page):
	def __init__(self):
		super(Game2, self).__init__()
		self.game2 = "Forget to Remember"
		self.game2Genre = "First Person Shooter"

		self._info2 = '''
		<p>Game Name: {self.game2}</p>
		<p>Game Genre: {self.game2Genre}</p>'''

	@property
	def info2(self):
		return self._info2

	def update(self):
		self._header = self._header.format(**locals())
		self._info2 = self._info2.format(**locals())