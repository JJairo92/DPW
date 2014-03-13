# Jairo Jurado
# DPW
# 03/13/2014
# Lab 3 - Encapsulated Calculator

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		# Tomb Raider (2013)
		self.tomb = Game()
		self.tomb.title = "Tomb Raider (2013)"
		self.tomb.ps3_sales = 1872139
		self.tomb.xbox360_sales = 1630789
		self.tomb.pc_sales = 248657
		self.tomb.ps4_sales = 293112
		self.tomb.xboxone_sales = 99107

		# Assassin's Creed IV
		self.acreed = Game()
		self.acreed.title = "Assassin's Creed IV: Black Flag"
		self.acreed.ps3_sales = 2714198
		self.acreed.xbox360_sales = 2392960
		self.acreed.pc_sales = 393637
		self.acreed.ps4_sales = 1434353
		self.acreed.xboxone_sales = 692308

# Data-Object Class
class Game(object):
	def __init__(self):
		self.title = ""
		self.ps3_sales = 0
		self.xbox360_sales = 0
		self.pc_sales = 0
		self.ps4_sales = 0
		self.xboxone_sales = 0

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)