print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
no_of_people = int(input("How many people to split the bill with? "))

amt_paid_by_each_person = round((total + ((tip_percentage/100) * total)) / no_of_people, 2)

print(f"Each person should pay: ${amt_paid_by_each_person}")