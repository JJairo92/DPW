# Jairo Jurado
# 01/29/2014
# DPW
# Final Exam - Music with XML

import webapp2
from page import *
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	page = Page()
        self.response.write(page.header + page.footer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)