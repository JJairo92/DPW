# Jairo Jurado
# 01/13/2014
# DPW
# Lab 3 Encapsulated Calculator

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)