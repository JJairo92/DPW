# Jairo Jurado
# 03/04/2014
# DPW
# Lab 1 - Madlib

# Array to hold strings
strings = []

# User's Name
name = raw_input("Enter your full name: ")

# Calculate age input variable and function
year_curr = 2014
year_born = input("In what year where you born? ") # "input" accepts integers

def calc_age(yc, yb):
	a = yc - yb
	return a
age = calc_age(year_curr, year_born)

print age

# Madlib
madlib = '''Test madlib'''

madlib = madlib.format(**locals())
print madlib