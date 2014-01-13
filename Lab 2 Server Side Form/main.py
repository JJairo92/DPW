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
    	</form>
    	'''

    	self.response.write(form)

    	self.response.write(page.close())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)