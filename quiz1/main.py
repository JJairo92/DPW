# Jairo Jurado
# 01/15/2014
# DPW
# Quiz 1

# Main Class
# class main(object):
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


# Beer Loop
beer = 99

def countDown(b):
	for b in range(0,100):
		loop = '''{b} Bottles of Beer on the Wall, {b} Bottles of Beer.. take one down and pass it around. Now you have {b} bottles of beer on the wall!'''
		loopFormatted = loop.format(**locals())
		print loopFormatted
countDown(beer)