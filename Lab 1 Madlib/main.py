# Jairo Jurado
# 03/04/2014
# DPW
# Lab 1 - Madlib

# Array to hold strings
strings = []

# User's Name
name = raw_input("Enter artist's stage name: ") # "raw_input" is for strings
strings.append(name) # adds "name" to strings array

# Gender; Pronoun function
gender = raw_input("Enter artist's gender: ")
if gender == "male" or gender == "Male":
	gender_pronoun = "He"
else:
	gender_pronoun = "She"
strings.append(gender_pronoun) # adds "gender_pronoun" to strings array

# Age function
year_curr = 2014
year_born = input("Enter the year the artist was born: ") # "input" accepts integers

def calc_age(yc, yb):
	age = yc - yb
	return age
a = calc_age(year_curr, year_born)

# Sales Estimate function
sales = input("Enter current album sales for artist: ")
popularity = raw_input("Does this person pass our popularity standards? (y/n) ")

if popularity == 'y' or popularity == 'Y':
	pop_bool = True
else:
	pop_bool = False

def calc_future_sales(sales, pop_bool):
	hispanic_states = 5
	usual_sales = 10000

	if pop_bool == True:
		pop_bonus = 20000
	else:
		pop_bonus = 0

	estimated_sales = sales + (usual_sales * 5) + pop_bonus
	return estimated_sales
est_sales = calc_future_sales(sales, pop_bool)

# Dictionary to hold numbers
numbers = dict()
numbers = dict(age=a,future_sales=est_sales,curr_sales=sales)
print numbers
print strings

# Madlib
madlib = '''I met an interesting person last night. {strings[1]} likes to be called {strings[0]} on stage. {strings[1]} is a singer and very well known in the hispanic community. We would like to get him to join our record company so he can reach the American community. We estimate '''

madlib = madlib.format(**locals())
print madlib