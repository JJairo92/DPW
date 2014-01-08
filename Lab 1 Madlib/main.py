# Jairo Jurado
# DPW
# 1/6/2014
# Madlib Lab

# Name
name = raw_input("Please type your name: ")

# Male/Female and the conditional for pronouns
gender = raw_input("Are you a male or a female? ")
if gender == "male" or gender == "Male":
	genderPronoun = "He"
else:
	genderPronoun = "She"

# 


# Madlib
madlib = '''I cannot believe how good of a friend {name} is. {genderPronoun} helped me with 
my physics homework. {genderPronoun} showed me the equation to find the Gravitational Force.
The equation is F8 = G(m1*m2/d^2); G being the gravitational constant, m1 being mass 1, m2
being mass 2, and d being distance.'''
madlibFormatted = madlib.format(**locals())

print madlibFormatted