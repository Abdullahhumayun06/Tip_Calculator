cost = float(input("What is the cost? "))
tax = int(input("What percentage tax should be added? "))

# This next line is here because for example, if the user says they want to tax 20%, I can't just multiply by 20 to give the final answer. Instead, I would have to multiply by 0.2
tax_multiplier = tax / 100
tax_amount = round(cost * tax_multiplier, 2)

tip = int(input("What percentage tip would you like to give? "))
tip_multiplier = tip / 100
tip_amount = round(cost * tip_multiplier, 2)

total_cost = round(cost + (cost * tip_multiplier) + (cost * tax_multiplier), 2)

print(f"The tax added is {tax_amount}")
print(f"The tip added is {tip_amount}")
print(f"Your total cost is {total_cost}" )