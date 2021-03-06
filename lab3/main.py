# Jairo Jurado
# DPW
# 03/13/2014
# Lab 3 - Encapsulated Calculator

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()

		# Tomb Raider (2013)
		self.tomb = Game()
		self.tomb.title = "Tomb Raider (2013)"
		self.tomb.ps3_sales = 1872139
		self.tomb.xbox360_sales = 1630789
		self.tomb.pc_sales = 248657
		self.tomb.ps4_sales = 293112
		self.tomb.xboxone_sales = 99107
		self.tomb.calc_total_sales()
		print "The total number of sales for " +self.tomb.title+ " is " +str(self.tomb.total_sales)

		# Assassin's Creed IV
		self.acreed = Game()
		self.acreed.title = "Assassin's Creed IV: Black Flag"
		self.acreed.ps3_sales = 2714198
		self.acreed.xbox360_sales = 2392960
		self.acreed.pc_sales = 393637
		self.acreed.ps4_sales = 1434353
		self.acreed.xboxone_sales = 692308
		self.acreed.calc_total_sales()
		print "The total number of sales for " +self.acreed.title+ " is " +str(self.acreed.total_sales)

		# CoD: Ghosts
		self.ghosts = Game()
		self.ghosts.title = "Call of Duty: Ghosts"
		self.ghosts.ps3_sales = 7539073
		self.ghosts.xbox360_sales = 8282936
		self.ghosts.pc_sales = 502961
		self.ghosts.ps4_sales = 1939980
		self.ghosts.xboxone_sales = 1566985
		self.ghosts.calc_total_sales()
		print "The total number of sales for " +self.ghosts.title+ " is " +str(self.ghosts.total_sales)

		# FIFA 14
		self.fifa = Game()
		self.fifa.title = "FIFA Soccer 14"
		self.fifa.ps3_sales = 5488401
		self.fifa.xbox360_sales = 3747307
		self.fifa.pc_sales = 244355
		self.fifa.ps4_sales = 1627931
		self.fifa.xboxone_sales = 779108
		self.fifa.calc_total_sales()
		print "The total number of sales for " +self.fifa.title+ " is " +str(self.fifa.total_sales)

		# Just Dance 2014
		self.jdance = Game()
		self.jdance.title = "Just Dance 2014"
		self.jdance.ps3_sales = 248065
		self.jdance.xbox360_sales = 749050
		self.jdance.pc_sales = 0 # game is not available for pc
		self.jdance.ps4_sales = 154497
		self.jdance.xboxone_sales = 196479
		self.jdance.calc_total_sales()
		print "The total number of sales for " +self.jdance.title+ " is " +str(self.jdance.total_sales)

		games = [self.tomb, self.acreed, self.ghosts, self.fifa, self.jdance]
		print games

		self.response.write(page.header + page.links)
		if self.request.GET:
			game = int(self.request.GET['game'])

			title = games[game].title
			ps3_sales = games[game].ps3_sales
			xbox360_sales = games[game].xbox360_sales
			pc_sales = games[game].pc_sales
			ps4_sales = games[game].ps4_sales
			xboxone_sales = games[game].xboxone_sales
			total_sales = games[game].total_sales

			info='''<div id="info">
			<h3>{title}</h3>
				<section id="sales">
					<p class="labels"><strong>PS3 Sales:</strong></p>
					<p class="labels"><strong>XBOX 360 Sales:</strong></p>
					<p class="labels"><strong>PC Sales:</strong></p>
					<p class="labels"><strong>PS4 Sales:</strong></p>
					<p class="labels"><strong>XBOX One Sales:</strong></p>
					<p class="labels"><strong>Total Sales:</strong></p>
				</section>

				<section id="numbers">
					<p class="stats">{ps3_sales}</p>
					<p class="stats">{xbox360_sales}</p>
					<p class="stats">{pc_sales}</p>
					<p class="stats">{ps4_sales}</p>
					<p class="stats">{xboxone_sales}</p>
					<p class="stats">{total_sales}</p>
				</section>
			</div>'''
			info = info.format(**locals())

			self.response.write(info)
		self.response.write(page.footer)


# Data-Object Class
class Game(object):
	def __init__(self):
		self.title = ""
		self.ps3_sales = 0
		self.xbox360_sales = 0
		self.pc_sales = 0
		self.ps4_sales = 0
		self.xboxone_sales = 0
		self.__total_sales = 0

	@property
	def total_sales(self):
		return self.__total_sales

	@total_sales.setter # setter
	def total_sales(self, sales):
		self.__total_sales = sales

	def calc_total_sales(self):
		total = self.ps3_sales + self.xbox360_sales + self.pc_sales + self.ps4_sales + self.xboxone_sales
		self.__total_sales = total

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)