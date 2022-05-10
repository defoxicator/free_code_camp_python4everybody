# Exercise 05_01
# Inputing numbers until "done" is the Input
# Managing non=numeric input as errors
# Printing sum, count and average

numbers = []
loop = 0
while loop == 0:
    user_input = input("> ")

    if user_input == "done":
        sum_of_numbers = sum(numbers)
        number_of_numbers = len(numbers)
        average_of_numbers = sum_of_numbers / number_of_numbers

        print("Sum: {}\nCount of numbers: {}\nAverage: {}".format(sum_of_numbers, number_of_numbers, average_of_numbers))
        loop += 1

    else:
        try:
            # converting input to float
            num = float(user_input)
            numbers.append(num)
        except:
            print("Wrong input")
