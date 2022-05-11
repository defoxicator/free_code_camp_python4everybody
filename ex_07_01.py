# Exercise 07_01
# Reading file and printing it in uppercase

file = open("mbox_short.txt", "r")
for line in file:
    print(line.upper())
