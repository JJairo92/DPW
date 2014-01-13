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
    		<label for="name">Name: </label>
    		<input class="input" type="text" placeholder="John Smith" /><br />

    		<label for="email">Email Address: </label>
    		<input class="input" type="email" placeholder="johnsmith@email.com" name="email"/><br />

    		<label for="system">What system information do you prefer?</label><br />
			<select class="input" name="system" id="system">
				<option>Console</option>
				<option>PC</option>
				<option>Mobile</option>
			</select><br />

    		<label for="agreement">Agreement:</label>
			<input class="input" type="checkbox" name="agreement" id="agreement" required="required" />I agree to sign-up for this newsletter.<br />
    		<input type="submit" value="Send" />
    	</form>
    	'''

    	self.response.write(form)

    	self.response.write(page.close())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)