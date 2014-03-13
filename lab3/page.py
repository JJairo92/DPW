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

		self.links = '''<a href="?game=0" name="link">Tomb Raider (2013)</a>
		<a href="?game=1" name="link">Assassin's Creed IV: Black Flag</a>
		<a href="?game=2" name="link">Call of Duty: Ghosts</a>
		<a href="?game=3" name="link">FIFA Soccer 2014</a>
		<a href="?game=4" name="link">Just Dance 2014</a>
		'''

		self.footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Game Sales</strong>. Number of sales taken from <a href="http://www.vgchartz.com" target="_blank">VG Charts</a></p>
		</footer>
	</html>'''

	def header(self):
		return self.header

	def links(self):
		return self.links

	def footer(self):
		return self.footer