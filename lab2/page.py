class Page():
	def __init__(self):
		self.__header = '''<!DOCTYPE>
	<html lang="en">
		<head>
			<title>Gamer Addictive | Newsletter Sign-Up</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
			<link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,600' rel='stylesheet' type='text/css'>
		</head>
		<body>
			<h1>Gamer Addictive Newsletter Sign-Up</h1>'''

		self.__footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Gamer Addictive</strong></p>
		</footer>
	</html>'''

	def open(self):
		return self.__header

	def close(self):
		return self.__footer