# Jairo Jurado
# 01/08/2014
# DPW
# Form Lab

import webapp2

from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	page = Page()

    	self.response.write(page.open())

    	form = '''
    	<form method="GET">
    		<label for="first-name">First Name:</label>
			<input class="input" type="text" name="first-name" id="first-name" autofocus="autofocus" placeholder="John" />

    		<label for="last-name">Last Name:</label>
			<input class="input" type="text" name="last-name" id="last-name" autofocus="autofocus" placeholder="Smith" />

    		<label for="email">Email Address: </label>
    		<input class="input" type="email" placeholder="johnsmith@email.com" name="email"/><br />

    		<label for="system">What system information do you prefer?</label>
			<select class="input" name="system" id="system">
				<option>Console</option>
				<option>PC</option>
				<option>Mobile</option>
			</select><br />
    		
			<input type="checkbox" name="agreement" id="agreement" required="required" />I agree to sign-up for this newsletter.<br />

    		<input type="submit" value="Send" />
    	</form>
    	'''

    	self.response.write(form)

    	self.response.write(page.close())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)