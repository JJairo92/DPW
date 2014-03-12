# Jairo Jurado
# DPW
# 03/11/2014
# Quiz 1

# Class to hold the functions
class MainClass(object):
	width = 5
	height = 5

	# Conditional to determine shape
	if width == height:
		shape = "square"
	else:
		shape = "rectangle"

	# calcArea function
	def calcArea(w,h):
		a = w * h
		return a
	area = calcArea(width,height)

	# Result in a Sentence
	print "The area of your " +shape+ " is " +str(area)+ " square feet."

	# Loop Function
	bottles = 99
	def countDown(bottles):
		beer = 99
		for bottles in range(100,0,-1):
			print str(bottles)+" Bottles of Beer on the Wall, "+str(bottles)+" Bottles of Beer.. take one down and pass it around. Now you have "+str(beer)+" bottles of beer on the wall!"
			beer -= 1
	countDown(bottles)