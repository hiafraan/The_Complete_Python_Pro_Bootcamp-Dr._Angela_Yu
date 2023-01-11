print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
last_total = (total * (percentage/100 + 1)) / split
last_total = round(last_total, 2)

last_total = "{:.2f}".format(last_total)
# how to round number to two decimel places

print("Each person should pay: $" + str(last_total))
