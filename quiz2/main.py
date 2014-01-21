# Jairo Jurado
# 01/20/2014
# DPW
# Quiz 2

class Formulas(object):
	#private properties
	_distance = 25
	_time = 5

	initialV = 10
	finalV = 20

	# Method to calculate acceleration
	def calcAcceleration(inV, fiV, t):
		acceleration = (fiV - inV) / t
		return acceleration
	a = calcAcceleration(initialV, finalV, _time)

	# Method/Function to calculate velocity
	def calcVelocity(d, t):
		velocity = d / t
		return velocity
	v = calcVelocity(_distance, _time)
	print v
	print a

	# "a" for "acceleration" / this is the getter
	@property
	def a():
		return a	
# second class (couldn't get it to accept parameters and it returns an error; class 1 works though)
class Force(Formulas):
	def __init__(self):
		Force = __init__(self)
		super(Force, self).__init__()
		mass = 5

		force = mass * a
		print a

Formulas()
Force()