# Jairo Jurado
# DPW
# 1/6/2014
# Madlib Lab

# Name
name = raw_input("Please type your friend's name: ") #raw_input will accept user inputs as strings

# Friend's age
age = input("How old is your friend? ")

friendClass = "Not known"
if age >= 18:
	friendClass = "adult"
else:
	friendClass = "not an adult yet"


# Male/Female and the conditional for pronouns
gender = raw_input("Is your friend a male or a female? ")
if gender == "male" or gender == "Male":
	genderPronoun = "He"
else:
	genderPronoun = "She"


# Velocity and Distance
distance = input("To find the velocity of something traveled, we need the distance. What is the distance? ") # "input" will check and look if the user input numbers
time = input("Now, what is the time of travel? ")

# Velocity function accepting 2 parameters, the distance and time
def calcVelocity(d, t):
	velocity = d / t
	return velocity
v = calcVelocity(distance, time)


# Acceleration
velInitial = input("To find the acceleration of something, we need the initial velocity, and the final velocity. What is the initial velocity? ")
velFinal = input("Now, what is the final velocity? ")

# Acceleration function accepting 3 parameters - inital velocity, final velocity, and time
def calcAcceleration(f, i, t):
	acceleration = (f - i) / t
	return acceleration
a = calcAcceleration(velFinal, velInitial, time) # time is the same one from the velocity formula


# Force
mass = input("To find the Force of something, we need the mass, what is the mass? ")

# Force function accepting 2 parameters - mass and acceleration
def calcForce(m, a):
	force = m * a
	return force
f = calcForce(mass, a)


# Arrays(Lists) and Objects(Dictionaries)
# All the variables from above will be added to an array or object
strings = [name, friendClass, genderPronoun]
numbers = dict()
numbers = dict(velocity=v, acceleration=a, force=f)

# Madlib
madlib = '''I cannot believe how good of a friend {strings[0]} is. {strings[2]} is considered {strings[1]}. {strings[2]} helped me with my physics homework. {strings[2]} showed me the equation to find the Velocity of something. The equation is velocity = distance / time. For example if the distance traveled is {distance}, and the time of travel is {time}; the velocity would be {v}. {strings[2]} also showed me the equation for Acceleration, which is Acceleration = (Velocity(Final) - Velocity(Initial)) / Time. For example if the Final Velocity is {velFinal}, the Initial Velocity is {velInitial}, and the time is {time}; the acceleration is {a}. {strings[2]} also showed me one last equation, the equation of Force, which is Force = Mass * Acceleration. If the mass is {mass}, and the acceleration is {a}; the force would be {f}.'''
madlibFormatted = madlib.format(**locals())

print madlibFormatted