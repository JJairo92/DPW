# Jairo Jurado
# DPW
# 03/13/2014
# Lab 4 - Animals

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)