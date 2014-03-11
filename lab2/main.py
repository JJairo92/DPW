# Jairo Jurado
# 03/11/2014
# DPW
# Lab 2 - Simple Form

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()

		if self.request.GET:
			first_name = self.request.GET['first-name']
			last_name = self.request.GET['last-name']
			email = self.request.GET['email']
			news_info = self.request.GET['system']

			result = '''<div id="results">
				<p>Thank you for signing up!</p>

				<p class="labels">First Name:</p>
				<p class="labels">Last Name:</p>
				<p class="labels">Email:</p>
				<p class="labels">Info you'd like to receive:</p>

				<p class="inputs">{first_name}</p>
				<p class="inputs">{last_name}</p>
				<p class="inputs">{email}</p>
				<p class="inputs">{news_info}</p>
			</div>'''

			result = result.format(**locals())

			self.response.write(page.header + result + page.footer)
		else:
			self.response.write(page.header + page.form + page.footer)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)