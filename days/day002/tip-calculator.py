print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What tip percentage would you like to give? 10, 12, or 15? "))
split_amount = int(input("How many people to split the bill? "))

result = (total_bill + (total_bill * tip_percentage / 100)) / split_amount

print(f"each person should pay ${'{:.2f}'.format(result)}")
