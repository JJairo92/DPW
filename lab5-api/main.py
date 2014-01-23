# Jairo Jurado
# 01/22/2014
# DPW
# Lab 5 API - League of Legends

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)