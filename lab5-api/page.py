class Page(object):
	def __init__(self):
		self.title = "Artist E.Lookup"
		self.css = '<link rel="stylesheet" type="text/css" href="css/main.css" />'
		self._header = '''<!DOCTYPE>
<html>
	<head>
		<meta charset="utf-8">
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

	

class Form(Page):
	def __init__(self):
		super(Form, self).__init__()

		self.method = "GET"
		self.action = ''
		self.__formOpen = '''
		<form action="{self.action}" method="{self.method}">'''

		self.__formClose = "</form>"

		@property
		def getForm(self):
			return self.__formOpen + self.__formClose

		def update(self):
			self._header = self._header.format(**locals())
			self.__formOpen = self.__formOpen.format(**locals())