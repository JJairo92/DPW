class Page():
	def __init__(self):
		self.header = '''<!DOCTYPE>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>Gamer Addictive | Newsletter Sign-Up</title>
			<link rel="stylesheet" href="css/main.css" type="text/css" />
			<link href='http://fonts.googleapis.com/css?family=Source+Code+Pro:400,600' rel='stylesheet' type='text/css'>
		</head>
		<body>
			<h1>Gamer Addictive Newsletter Sign-Up</h1>'''

		self.form = '''<form method="GET">
			<label for="first-name">First Name:</label>
			<label for="last-name">Last Name:</label>
			<label for="email">Email Address: </label>
			<label for="system">Information in Newsletter?</label>

			<input class="input" type="text" name="first-name" id="first-name" autofocus="autofocus" placeholder="John" />
			<input class="input" type="text" name="last-name" id="last-name" placeholder="Smith" />
			<input class="input" type="email" placeholder="johnsmith@email.com" name="email" id="email" /><br />

			<select class="input" name="system" id="system">
				<option>Console</option>
				<option>PC</option>
				<option>Mobile</option>
				<option>Everything</option>
			</select><br />
			
			<div id="checkbox">
				<input type="checkbox" name="agreement" id="agreement" required="required" />I agree to sign-up for this newsletter.<br />
			</div>
			
			<input type="submit" value="Sign-Up!" />
		</form>
		'''

		self.footer = '''
		</body>

		<footer>
			<p>Copyright &copy; 2014 <strong>Gamer Addictive</strong></p>
		</footer>
	</html>'''

	def header(self):
		return self.header

	def form(self):
		return self.form

	def footer(self):
		return self.footer