# MY SOLUTION USING FOR/WHILE

purchase = float(input("Please enter the total due on the purchase: "))
given = float(input("Please also enter the cash given for the purchase: "))
if given < purchase:
    print("Please give cash greater than the purchase total.")
    while given < purchase:
        try: given = float(input(": "))
        except: print("Invalid input.")
change = given - purchase

denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
change_returned = []
for denomination in denominations:
    while change >= denomination:
        change_returned.append(denomination)
        change = change - denomination
print(change_returned)