# Exercise 04_06
# Rewriting the Exercise 03_02 to form a function

def computepay(hours, rate):
    try:
        if hours > 40:
            hours_above = hours - 40
            bonus_rate = rate * 1.5
            bonus_payment = hours_above * bonus_rate
        else:
            bonus_payment = 0

        print("Your pay:", hours * rate + bonus_payment)

    except:
            print("Please enter numeric input.")

computepay(42, 42)
