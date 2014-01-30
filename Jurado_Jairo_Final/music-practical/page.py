class MusicView(object):
	def __init__(self, do):
		for song in do.songs:
			self.__content = '<h3>' +song[0]+ '</h3>'

	@property
	def content(self):
		return self.__content

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
				<h1>Music App</h1>
				<ul>
					<li>Good Vibrations</li>
					<audio src="mp3s/Good_Vibrations.mp3" controls="controls"></audio><br />
					<li>Hey Jude</li>
					<audio src="mp3s/Hey-Jude.mp3" controls="controls"></audio>
					<li>Imagine</li>
					<audio src="mp3s/imagine.mp3" controls="controls"></audio>
					<li>Rolling Stone</li>
					<audio src="mp3s/rollingstone.mp3" controls="controls"></audio>
					<li>Smells Like Teen Spirit</li>
					<audio src="mp3s/smells-like-teen-spirit.mp3" controls="controls"></audio>
					<li>What's Going On</li>
					<audio src="mp3s/WhatsGoingOn.mp3" controls="controls"></audio></ul>'''

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


class Form(Page):
	def __init__(self, obj):
		super(Form, self).__init__()

		self.method = 'GET'
		self.action = ''

		self.__formOpen = '''
		<form action="{self.action}" method="{self.method}">'''
		self.__links = ''
		for el in obj:
			self.__links += '<button>{el[song]}</button>'
			self.__links = self.__links.format(**locals())

		self.__formClose = '</form>'

	@property
	def getForm(self):
		return self.__formOpen + self.__links + self.__formClose

	def update(self):
		self._header = self._header.format(**locals())
		self.__formOpen = self.__formOpen.format(**locals())