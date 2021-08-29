# SOLUTION USING IF/ELIF/ELSE

# ALGORITHM THAT GETS PURCHASE TOTAL AND GIVEN CASH, AND CALCULATES CHANGE DUE. IF GIVEN AMOUNT
# IS LESS THAN PURCHASE TOTAL, IT PROMPTS THE USER TO GIVE CASH GREATER THAN THE TOTAL DUE.

purchase = float(input("Please enter the total due on the purchase: "))
given = float(input("Please also enter the cash given for the purchase: "))
if given < purchase:
    print("Please give cash greater than the purchase total.")
    while given < purchase:
        try: given = float(input(": "))
        except: print("Invalid input.")
change = given - purchase

# FOR DEBUGGING PURPOSES
debugger = change # I know I don't have to do this, but I just wanted to do.
print("---\n", f"Change due is {debugger}", end="\n---\n")
change = debugger

# ALGORTHM PROPER--COUNTING CHANGE ALGORITHM

# Starting banknotes.
print("Change given: ", end="")

if (change // 100) > 1: print(int(change // 100), "hundreds", end=", ")
elif (change // 100) == 1: print("An one (1) hundred", end=", ")
change = change % 100

if (change // 50) == 1 or change == 50: print("one (1) fifty", end=", ")
change = change % 50

if (change // 20) > 1: print(int(change // 20), "twenties", end=", ")
elif (change // 20) == 1: print("one (1) twenty", end=", ") 
change = change % 20
    
if (change // 10) == 1 or change == 10: print("one (1) ten", end=", ")
change = change % 10

if (change // 5) == 1 or change == 5: print("one (1) five", end=", and ")
change = change % 5

if (change // 1) > 1: print(int(change // 1), "ones", end=" in cash. ")
elif (change // 1) == 1: print("an one (1) in cash", end=". ")
change = change % 1
    
# Finally, coins.
change = change * 100
if (change // 25) > 1: print("And in change, ", int(change // 25), "quarters,", end=", ")
elif (change // 25) == 1: print("And in change, one (1) quarter", end=", and")