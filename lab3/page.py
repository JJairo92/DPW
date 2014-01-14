class Page():
	def __init__(self):
		self.__header = '''<!DOCTYPE>
	<html lang="en">
		<head>
			<title>Data Objects</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
		</head>
		<body>
			<h1>Data Objects</h1>'''

		self.__footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Data Objects</strong></p>
		</footer>
	</html>'''

	def open(self):
		return self.__header

	def close(self):
		return self.__footer