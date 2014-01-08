# Jairo Jurado
# DPW
# 1/6/2014
# Madlib Lab

# Name
name = input("Please type your name: ")

# Male/Female and the conditional for pronouns
gender = input("Are you a male or a female? ")
if gender == "male" or gender == "Male":
	genderPronoun = "He"
else:
	genderPronoun = "She"

# Velocity and Distance
distance = input("To find the velocity of something traveled, we need the distance. What is the distance? ")
time = input("Now, what is the time of travel? ")
# Velocity function accepting 2 parameters, the distance and time
def calcVelocity(d, t):
	velocity = d / t
	return velocity
v = calcVelocity(distance, time)


# Madlib
madlib = '''I cannot believe how good of a friend {name} is. {genderPronoun} helped me with my physics homework. {genderPronoun} showed me the equation to find the Velocity of something. The equation is velocity = distance / time. For example if the distance traveled is {distance}, and the time of travel is {time}; the velocity would be {v}.'''
madlibFormatted = madlib.format(**locals())

print madlibFormatted