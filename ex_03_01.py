# Excercise 03_01
# Addition of new features to Excercise 02_03

hours = float(input("Enter no. of hours: "))
rate = float(input("Enter payment per hour: "))

if hours > 40:
    hours_above = hours - 40
    bonus_rate = rate * 1.5
    bonus_payment = hours_above * bonus_rate
else:
    bonus_payment = 0

print("Your pay:", hours * rate + bonus_payment)
