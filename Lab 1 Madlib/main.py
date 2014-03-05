# Jairo Jurado
# 03/04/2014
# DPW
# Lab 1 - Madlib

# User's Name
name = raw_input("Enter your full name: ")
print name

# Madlib
madlib = '''Test madlib'''

madlib = madlib.format(**locals())
print madlib