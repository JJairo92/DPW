class View(object):
	def __init__(self):
		self.__content = ''

class Page(object):
	def __init__(self):
		self.title = "Music App"
		self._header = '''<!DOCTYPE>
		<html>
			<head>
				<meta charset="utf-8">
				<title>{self.title}</title>
			</head>
			<body>
				<h1>Music App</h1>'''

		self.__footer = '''
			</body>
		</html>'''

	@property
	def header(self):
		return self._header