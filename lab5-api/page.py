class ArtistView(object):
	def __init__(self, do):
		self.__content = '<h2>' + do.artist + '</h2>'
		for event in do.events:
			self.__content += '<div class="event"><div class="venues"><h3>Venue</h3><p>'+event[0]+'</p></div>' + '<div class="cities"><h3>City</h3><p>'+event[1]+'</p></div>' + '<div class="regions"><h3>State/Region</h3><p>'+event[2]+'</p></div>' + '<div class="countries"><h3>Country</h3><p>'+event[3]+'</p></div></div>'

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
		<link href='http://fonts.googleapis.com/css?family=Crimson+Text:400,700italic|Rock+Salt' rel='stylesheet' type='text/css'>
	</head>
	<body>
		<h1>Artist E. Lookup</h1>
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
			self.__inputs += '<div id="search-box"><input type="{el[type]}" value="{el[label]}" name="{el[name]}"></input></div>'
			self.__inputs = self.__inputs.format(**locals())

		self.__formClose = "</form>"

	@property
	def getForm(self):
		return self.__formOpen + self.__inputs + self.__formClose

	def update(self):
		self._header = self._header.format(**locals())
		self.__formOpen = self.__formOpen.format(**locals())