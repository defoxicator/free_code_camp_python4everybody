# Excercise 04_06
# Rewriting the Excercise 03_02 to form a function

def computepay():
    loop = 0
    while loop == 0:
        try:
            hours = float(input("Enter no. of hours: "))
            rate = float(input("Enter payment per hour: "))
            loop += 1
        except:
            print("Please enter numeric input.")

    if hours > 40:
        hours_above = hours - 40
        bonus_rate = rate * 1.5
        bonus_payment = hours_above * bonus_rate
    else:
        bonus_payment = 0

        print("Your pay:", hours * rate + bonus_payment)

computepay()
