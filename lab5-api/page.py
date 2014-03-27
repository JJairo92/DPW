class Page(object):
	def __init__(self):
		self.header = '''<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>Artist E.Lookup</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
			<link href='http://fonts.googleapis.com/css?family=Fondamento:400,400italic|Lato' rel='stylesheet' type='text/css'>
		</head>
		<body>
			<div id="container">
			<h1><img src="images/logo.png" /></h1>'''

		self.form = '''<form method="GET">
		<input id="search-box" type="text" name="artist" autofocus="autofocus" placeholder="Search artist" required="required" />
			
		<input type="submit" value="Get Events!" />
		</form>
		'''

		self.footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Artist E.Lookup.</strong> This is a fictional company.</p>
		</footer>
		</div> <!-- Closes "container" div -->
	</html>'''

	def header(self):
		return self.header

	def form(self):
		return self.form

	def footer(self):
		return self.footer