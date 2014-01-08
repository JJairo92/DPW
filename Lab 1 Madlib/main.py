# Jairo Jurado
# DPW
# 1/6/2014
# Madlib Lab

# Name
name = raw_input("Please type your name: ")

# Madlib
message = '''I cannot believe how good of a friend {name} is.'''
messageFormatted = message.format(**locals())

print messageFormatted