# Jairo Jurado
# DPW
# 03/13/2014
# Quiz 2

# The instructions for this quiz are very confusing; I think you wanted to methods and the "def" used in the property will count as one of them, that's why I added one more "def" to class Student

class Student(object):
	_first_name = 'Jairo'
	_last_name = 'Jurado'
	username = 'JJairo92'
	new_games = 4
	used_games = 2

	@property
	def first_name(self):
		return _first_name

	def calc_total_games(ng, ug): # method with 2 parameters
		total = ng + ug
		return total
	total_games = calc_total_games(new_games, used_games)

	print _first_name+ " " +_last_name+ " has a total of " +str(total_games)+ " games."

class House(object):
	windows = 2
	rooms = 3