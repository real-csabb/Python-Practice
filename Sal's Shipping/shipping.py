# VARIABLES
package = input("Enter package's weight: ")
package = float(package)

# GROUND SHIPPING ALGORITHM
if package > 10.00:
  ground_cost = (package * 4.75) + 20.00
elif package > 6 and package <= 10:
  ground_cost = (package * 4.00) + 20.00
elif package > 2 and package <= 6:
  ground_cost = (package * 3.00) + 20.00
else:
  ground_cost = (package * 1.50) + 20.00

# DRONE SHIPPING ALGORITHM
if package > 10.00:
  drone_cost = (package * 14.25)
elif package > 6 and package <= 10:
  drone_cost = (package * 12.00)
elif package > 2 and package <= 6:
  drone_cost = (package * 9.00)
else:
  drone_cost = (package * 4.50)

# PRINT STATEMENTS
print(f"""\nGround Shipping Cost: ${ground_cost}\n
Ground Shipping Premium: $125.00\n
Drone Shipping Cost: ${drone_cost}""")