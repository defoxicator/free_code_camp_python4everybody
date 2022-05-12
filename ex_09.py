# Exercise 09
# Stripping the text file and counting the amount of every word
# Finding most common word

file_name = input("Enter file: ")
if len(file_name) < 1: file_name = "clown.txt"

file_handle = open(file_name)

dictionary = dict()
for line in file_handle:
    line = line.strip()
    words = line.split()

    for word in words:
        # idiom: retrieve/create/update counter
        dictionary[word] = dictionary.get(word, 0) + 1

# the loop through key: value pairs
largest = -1
most_common_word = None
for key, value in dictionary.items():

    if value > largest:
        largest = value
        #capture and remember the most common word
        most_common_word = key

print("The most common word is:", most_common_word, "with cthe ount of:", largest)
