# Jairo Jurado
# DPW
# 03/20/2014
# Quiz 3

import webapp2

# Abstract Class
class VideoGame(webapp2.RequestHandler):
	def get(self):
		self._name = "Name"
		self._genre = "Genre" #protected attribute

		# uncomment below to check that attributes are overwritten
		# kill = Kill()
		# self.response.write(kill.name+"<br />" +kill.genre+"<br />" +kill.developer+"<br />")

		# live = Live()
		# self.response.write(live.name+"<br />" +live.genre+"<br />" +live.publisher+"<br />")

	@property
	def name(self): #method 1 (quiz instructions did not say "in addition to property methods")
		return self._name

	@property
	def genre(self): #method 2 (quiz instructions did not say "in addition to property methods")
		return self._genre

# Subclass 1
class Kill(VideoGame):
	def __init__(self):
		super(Kill, self).__init__()
		self._name = "Kill to Live"
		self._genre = "Third Person Shooter"
		self._developer = "Unshaken Studios"
		self._publisher = "Life+Death"

	@property
	def developer(self): #additional property for subclass
		return self._developer

# Subclass 2
class Live(VideoGame):
	def __init__(self):
		super(Live, self).__init__()
		self._name = "Live to Kill"
		self._genre = "RPG"
		self._developer = "Trident Souls"
		self._publisher = "Perfected Forever"

	@property
	def publisher(self): # additional property for subclass
		return self._publisher

app = webapp2.WSGIApplication([
	('/', VideoGame)
], debug=True)