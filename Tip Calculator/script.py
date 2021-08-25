# You just finished eating at a restaurant and received this bill...
costOfMeal = float(input("\nHow much is the bill? " or 44.50)) # Default: $44.50
restaurantTax = 0.0675 # Read: 6.75%
tip = 0.15 # Read: 15%

""" Algorithm takes the cost of your meal and mutiplies it by the amount 
of taxes and tip and adds it all together. """
costOfTax = costOfMeal * restaurantTax
costOfTip = costOfMeal * tip
total = costOfMeal + costOfTax + costOfTip
print(f"""\nYou owe ${total} in total for your meal. There is a tax of ${costOfTax} and a 
${costOfTip} tip.""")