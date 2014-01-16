# Jairo Jurado
# 01/15/2014
# DPW
# Quiz 1

# Area Calculation
width = 5
height = 7
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

message = '''The area of your {shape} is {a} square feet.'''
messageFormatted = message.format(**locals())

print messageFormatted