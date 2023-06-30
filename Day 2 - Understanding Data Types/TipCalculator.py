#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
num_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? ")) / 100
#Each person should pay (150.00 / 5) * 1.12 = 33.6
result = (bill / num_people) * (1 + tip)
#Format the result to 2 decimal places = 33.60
rounded_result = "{:.2f}".format(result)
print(f"Each person should pay: ${rounded_result}")
