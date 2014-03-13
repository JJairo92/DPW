class Page():
	def __init__(self):
		self.header = '''<!DOCTYPE>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>Game Sales</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
		</head>
		<body>
			<h1>Game Sales</h1>'''

		self.links = '''<a href="?game=tomb">Tomb Raider(2013)</a>
		'''

		self.footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Game Sales</strong></p>
			<small>Number of sales taken from<a href="http://www.vgchartz.com" target="_blank">VG Charts</a></small>
		</footer>
	</html>'''

	def header(self):
		return self.header

	def links(self):
		return self.links

	def footer(self):
		return self.footer