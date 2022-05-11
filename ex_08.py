# Exercise 08
# Reading file and printing it in uppercase

file = open("mbox_short.txt", "r")
for line in file:
    line = line.strip()
    words = line.split()
    if len(words) > 0:
        if words[0] != "From":
            continue
        print(words[2])
