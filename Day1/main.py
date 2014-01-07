# Jairo Jurado
# DPW
# 1/6/2014

print "Hello World"
"""
This is where I am learning about cool python syntax like variables, expressions, conditionals, loop functions
"""

#single lined comment

#basic variables
firstName = "Jairo"
lastName = "Jurado"
print firstName + ' ' + lastName

yearBorn = 1992
age = 2014 - yearBorn
print age
#print firstName + ", you are " + str(age) + " years old"

#format string function
message = '''{firstName}, you are {age} years old'''
messageFormatted = message.format(**locals())
#print messageFormatted

#expressions
numPears = 6
#same as js

# #conditionals -if
# if numPears == 6:
# 	print "I have 6 pears"
# 	print "I love my pears"

# # if else
# if numPears <6:
# 	print "I have less than six pears"
# else:
# 	print "I have 6 pears or more"

# # else if
# if numPears == 2:
# 	print "duo pears!"
# else:
# 	print "you have something other than 1 or 2 pears"


#Arrays - called "lists" in python
races = ["protoss", "zerg", "terran"]
races.append("Xul'Naga")
print races
#races.pop() - removes last item on the array/list
races.reverse() #prints array in reversed order
#print races[1:3] #from ___ to : ___
print races

#dictionaries - associative arrays python - object
#data structures

#TV shows of students in DPW
shows = dict() #intantiating function
shows = dict(Ross="Bones", Russell="Scrubs", Jairo="How I Met Your Mother")
shows2 = { "Nate": "BoardwalkEmpire" , "Anthony" : "House" }
shows3 = dict()
shows3["Mike"] = "Hostages"
shows3["Tyrone"] = "Sons of Anarchy"
#print shows3["Tyrone"]


#Functions
#variable created outside... scoped global
height = 60
width = 2

def calcArea(h, w): #implies h = height, w = width
	area = h * w #variables in functions.. scoped to functions
	return area

a = calcArea(height, width)
print a

def calcPerimeter():
	pass #"pass" will fill empty space for structural use (it will not freak out)


#Loops
#for(var i=0; i<3; i++) in js
#for race in races:
	#print race

for i in range(0,10):
	#print "before" + str(i)
	i = i-2
	#print i #find count neg

#random
import random

for i in range(0,100):
	rand = random.randrange(2,9)
	print str(rand) + " is the random number. This is the " + str(i+1) + "th time"
	if rand == 8:
		break

#Inputs
name = input("Type in your name.")
print name