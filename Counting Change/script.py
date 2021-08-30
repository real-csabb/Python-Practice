# ALGORITHM THAT GETS PURCHASE TOTAL AND GIVEN CASH, AND CALCULATES CHANGE DUE. IF GIVEN AMOUNT
# IS LESS THAN PURCHASE TOTAL, IT PROMPTS THE USER TO GIVE CASH GREATER THAN THE TOTAL DUE.

purchase = float(input("Please enter the total due on the purchase: "))
if purchase <= 0:
    print("Please enter a number greater than zero.")
    while purchase <= 0:
        try: purchase = float(input(": "))
        except: print("Invalid input.")
given = float(input("Please also enter the cash given for the purchase: "))
if given < purchase:
    print("Please give cash greater than the purchase total.")
    while given < purchase or given <= 0:
        try: given = float(input(": "))
        except: print("Invalid input.")
change = given - purchase

# CASH
if (change // 100) >= 1: print((change // 100), "$100 Bills.")
change = change % 100
if (change // 50) >= 1: print((change // 50), "$50 Bills.")
change = change % 50
if (change // 20) >= 1: print(int(change // 20), "$20 Bills.")
change = change % 20
if (change // 5) >= 1: print(int(change // 5), "Fives.")
change = change % 5
if (change // 1) >= 1: print(int(change // 1), "Dollar Bills.")
change = change % 1

# CHANGE
change = round(change * 100)
if (change // 25) >= 1: print(int(change // 25), "Quarters.")
change = change % 25
if (change // 5) >= 1: print(int(change // 5), "Nickels.")
change = change % 5
if (change // 1) >= 1: print(int(change // 1), "Pennies.")
change = change % 1