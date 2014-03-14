# Jairo Jurado
# DPW
# 03/13/2014
# Quiz 2
'''
The instructions for this quiz are very confusing; I think you wanted to methods and the "def" used in the property will count as one of them, that's why I added one more "def" to class Student, and one more property just in case.'''

class Student(object):
	_first_name = 'Jairo'
	_last_name = 'Jurado'
	username = 'JJairo92'
	new_games = 4
	used_games = 2

	@property
	def first_name(self):
		return _first_name

	@property
	def last_name(self):
		return _last_name

	def calc_total_games(ng, ug): # method with 2 parameters
		total = ng + ug
		return total
	total_games = calc_total_games(new_games, used_games)

	print _first_name+ " " +_last_name+ " has a total of " +str(total_games)+ " games."

'''For class House, I think the setter would've worked just fine in Google App Engine, I'm very positive it is how you showed us. I don't know why the "windows" number is not being replaced by "__new_windows". From what I understood, you wanted 2 methods in this class and one of them had to be outisde the property. The instructions were also a little confusing, either way, this is as far as I got.'''

class House(object):
	windows = 2
	rooms = 3

	__new_windows = 4

	@property
	def new_windows(self):
		return __new_windows

	@new_windows.setter
	def new_windows(self, nw):
		windows = nw

	def calc_windows_per_room(w, r):
		t = w * r
		return t
	total_windows = calc_windows_per_room(windows, rooms)

	print total_windows