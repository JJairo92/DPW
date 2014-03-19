class Page(object):
	def __init__(self):
		self.header = '''<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>API | Artist e.Lookup</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
			<link href='http://fonts.googleapis.com/css?family=Fondamento:400,400italic|Lato' rel='stylesheet' type='text/css'>
		</head>
		<body>
			<div id="container">
			<h1>API</h1>'''

		self.__form = '''<form method="GET">
			<label for="artist">Artist:</label>

			<input type="text" name="artist" autofocus="autofocus" placeholder="Search artist" />
			
			<input type="submit" value="Get Events!" />
		</form>
		'''

		self.footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>API.</strong></p>
		</footer>
		</div> <!-- Closes "container" div -->
	</html>'''

	def header(self):
		return self.header

	def form(self):
		return self.__form

	def footer(self):
		return self.footer