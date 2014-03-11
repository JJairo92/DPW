# Jairo Jurado
# 03/11/2014
# DPW
# Lab 2 - Simple Form

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()

        self.response.write(page.header + page.footer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)