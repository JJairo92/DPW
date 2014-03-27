# Jairo Jurado
# DPW
# 03/27/2014
# Music Practical

import webapp2

class MusicController(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MusicController)
], debug=True)