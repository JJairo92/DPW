# Jairo Jurado
# 01/15/2014
# DPW
# Quiz 1

# Area Calculation
width = 5
height = 5
shape = ''

# Conditional for determining whether shape is a rectangle or a square
if width == height:
	shape = "square"
else:
	shape = "rectangle"

# Area Function
def calcArea(w, h):
	area = w * h
	return area
a = calcArea(width, height)