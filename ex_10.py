# Exercise 10
# Searching for 5 most common words

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

most_common = sorted( [ (value, key) for key, value in dictionary.items() ] )[::-1]

pretty_list = []

for item in most_common:
    pretty_list.append(item[1])
print("The five most common words are:", pretty_list[:5])
