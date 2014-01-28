class ArtistView(object):
	def __init__(self, getArtist):
		self.__content = '<h3>' + getArtist.title + '</h3>'

	@property
	def content(self):
		return self.__content

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
	def __init__(self, obj):
		super(Form, self).__init__()

		self.method = "GET"
		self.action = ''
		self.__formOpen = '''
		<form action="{self.action}" method="{self.method}">'''

		self.__inputs = ''
		for el in obj: # "el" for element in object(obj)
			self.__inputs += '<input type="{el[type]}" placeholder="{el[label]}" name="{el[name]}"></input>'
			self.__inputs = self.__inputs.format(**locals())

		self.__formClose = "</form>"

	@property
	def getForm(self):
		return self.__formOpen + self.__inputs + self.__formClose

	def update(self):
		self._header = self._header.format(**locals())
		self.__formOpen = self.__formOpen.format(**locals())