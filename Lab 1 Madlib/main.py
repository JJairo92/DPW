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


# Madlib
message = '''I cannot believe how good of a friend {name} is. {genderPronoun} helped me with 
my homework.'''
messageFormatted = message.format(**locals())

print messageFormatted