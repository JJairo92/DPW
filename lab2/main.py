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
    		<label for="last-name">Last Name:</label>
    		<label for="email">Email Address: </label>
    		<label for="system">Information in Newsletter?</label>


			<input class="input" type="text" name="first-name" id="first-name" autofocus="autofocus" placeholder="John" />
			<input class="input" type="text" name="last-name" id="last-name" autofocus="autofocus" placeholder="Smith" />
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
    		<input type="submit" value="Send" />
    	</form>
    	'''

    	self.response.write(form)

    	self.response.write(page.close())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)