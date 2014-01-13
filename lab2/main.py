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
    		<input type="text" placeholder="John Smith" /><br />

    		<label for="email">Email Address: </label>
    		<input type="email" placeholder="johnsmith@email.com" name="email"/><br />

    		<label for="system">What system information do you prefer?</label>
			<select name="system" id="system">
				<option>Console</option>
				<option>PC</option>
				<option>Mobile</option>
			</select>
    	</form>
    	'''

    	self.response.write(form)

    	self.response.write(page.close())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)