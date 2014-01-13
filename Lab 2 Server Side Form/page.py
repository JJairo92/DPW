class Page():
	def __init__(self):
		self.__header = '''<!DOCTYPE>
	<html lang="en">
		<head>
			<title>Gamer Addictive | Newsletter Sign-Up</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
		</head>
		<body>
			<h1>Gamer Addictive Newsletter Sign-Up</h1>'''

		self.__footer = '''
		</body>
	</html>'''

	def open(self):
		return self.__header

	def close(self):
		return self.__footer