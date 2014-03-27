class Page(object):
	def __init__(self):
		self.header = '''<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>Music Practical</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
		</head>
		<body>
			<h1>Music Practical</h1>'''

		self._footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Music Practical.</strong></p>
		</footer>
	</html>'''

	def header(self):
		return self.header

	def footer(self):
		return self._footer