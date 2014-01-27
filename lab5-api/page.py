class Page(object):
	def __init__(self):
		self.title = "League of Legends Stats"
		self.css = '<link rel="stylesheet" type="text/css" href="css/main.css" />'
		self._header = '''<!DOCTYPE>
<html>
	<head>
		<title>{self.title}</title>
		{self.css}
	</head>
	<body>
'''
		self.__footer = '''
	</body>
</html>'''

	@property
	def header(self):
		return self._header

	@property
	def footer(self):
		return self.__footer

	def update(self):
		self._header = self._header.format(**locals())