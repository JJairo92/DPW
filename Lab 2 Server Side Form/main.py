# Jairo Jurado
# 01/08/2014
# DPW
# Form Lab

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	form = '''
    	<form method="GET" action="">
    		
    	</form>
    	'''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)