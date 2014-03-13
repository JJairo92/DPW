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

		# CoD: Ghosts
		self.ghosts = Game()
		self.ghosts.title = "Call of Duty: Ghosts"
		self.ghosts.ps3_sales = 7539073
		self.ghosts.xbox360_sales = 8282936
		self.ghosts.pc_sales = 502961
		self.ghosts.ps4_sales = 1939980
		self.ghosts.xboxone_sales = 1566985

		# FIFA 14
		self.fifa = Game()
		self.fifa.title = "FIFA Soccer 14"
		self.fifa.ps3_sales = 5488401
		self.fifa.xbox360_sales = 3747307
		self.fifa.pc_sales = 244355
		self.fifa.ps4_sales = 1627931
		self.fifa.xboxone_sales = 779108

		# Just Dance 2014
		self.jdance = Game()
		self.jdance.title = "Just Dance 2014"
		self.jdance.ps3_sales = 248065
		self.jdance.xbox360_sales = 749050
		self.jdance.pc_sales = 0 # game is not available for pc
		self.jdance.ps4_sales = 154497
		self.jdance.xboxone_sales = 196479

# Data-Object Class
class Game(object):
	def __init__(self):
		self.title = ""
		self.ps3_sales = 0
		self.xbox360_sales = 0
		self.pc_sales = 0
		self.ps4_sales = 0
		self.xboxone_sales = 0
		self.total_sales = 0

	def calc_total_sales(self):
		total = self.ps3_sales + self.xbox360_sales + self.pc_sales + self.ps4_sales + self.xboxone_sales
		self.total_sales = total

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)