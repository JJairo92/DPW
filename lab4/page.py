class Page(object):
	def __init__(self):
		self.header = '''<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>Animals</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
			<link href='http://fonts.googleapis.com/css?family=Fondamento:400,400italic|Lato' rel='stylesheet' type='text/css'>
		</head>
		<body>
			<div id="container">
			<h1>Animals</h1>'''

		self.links = '''<nav>
		<ul>
			<li><a href="?animal=0" class="links">Puma</a></li>
			<li><a href="?animal=1" class="links">Bear</a></li>
			<li><a href="?animal=2" class="links">Wolf</a></li>
		</ul>
		</nav>
		'''

		self.footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Animals.</strong></p>
		</footer>
		</div> <!-- Closes "container" div -->
	</html>'''

	def header(self):
		return self.header

	def links(self):
		return self.links

	def footer(self):
		return self.footer