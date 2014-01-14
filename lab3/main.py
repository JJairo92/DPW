# Jairo Jurado
# 01/13/2014
# DPW
# Lab 3 Encapsulated Calculator

import webapp2

from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()

    	self.response.write(page.open())

    	self.response.write(page.close())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)