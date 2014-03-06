# Jairo Jurado
# 03/04/2014
# DPW
# Lab 1 - Madlib

# Array to hold strings
strings = []

# User's Name
name = raw_input("Enter your full name: ") # "raw_input" is for strings

# Calculate age input variable and function
year_curr = 2014
year_born = input("In what year where you born? ") # "input" accepts integers

def calc_age(yc, yb):
	a = yc - yb
	return a
age = calc_age(year_curr, year_born)
strings.append(age)

# Conditional to check legal drinking age
legal_drinker = False # "True" if legal drinker; the conditional will determine it
if age >= 21:
	legal_drinker = True
else:
	legal_drinker = False

# Calculate

print age

# Madlib
madlib = '''I met'''

madlib = madlib.format(**locals())
print madlib