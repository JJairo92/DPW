class Page(object):
	def __init__(self):
		self.header = '''<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>Animals</title>
		</head>
		<body>
			<div id="container">
			<h1>Animals</h1>'''

		self.links = '''<a href="?animal=0" class="links">Puma</a>
		<a href="?animal=1" class="links">Bear</a>
		<a href="?animal=2" class="links">Wolf</a>
		'''