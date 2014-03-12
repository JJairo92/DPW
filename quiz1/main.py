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