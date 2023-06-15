# Tip calculator project
message = "Welcome to the tip calculator"
print(message)

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
people_amount = int(input("How many people to split the bill? "))

splited_amount = (total_bill + (total_bill * tip_percentage / 100)) / people_amount
rounded_amount = "{:.2f}".format(round(splited_amount, 2))

print(f"Each person should pay ${rounded_amount}")
