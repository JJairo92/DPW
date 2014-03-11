# Jairo Jurado
# 03/11/2014
# DPW
# Lab 2 - Simple Form

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)