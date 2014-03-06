# Jairo Jurado
# 03/04/2014
# DPW
# Lab 1 - Madlib

# Array to hold strings
strings = []

# User's Name
name = raw_input("Enter person's full name: ") # "raw_input" is for strings


# Gender; Pronoun function
gender = raw_input("Enter person's gender: ")
if gender == "male" or gender == "Male":
	gender_pronoun = "He"
else:
	gender_pronoun = "She"



# Calculate age input variable and function
year_curr = 2014
year_born = input("Enter the year the person was born: ") # "input" accepts integers

def calc_age(yc, yb):
	age = yc - yb
	return age
a = calc_age(year_curr, year_born)

# Conditional to check legal drinking age
if a >= 21:
	legal_drinker = True
else:
	legal_drinker = False

# Dictionary to hold numbers
numbers = dict()
numbers = dict(age=a)
print numbers
print strings

# Madlib
madlib = '''I met an interesting person last night. {strings[1]}'''

madlib = madlib.format(**locals())
print madlib