# Exercise 06_05
# Exctracting parts of the string

# This is given string and the float need to be extracted as floating point number
str = "X-DSPAM-Confidence: 0.8475 "
position = str.find(":")
needed_info = str[position + 2:]
number = float(needed_info)
# now number can be used in calculations

print(number)
