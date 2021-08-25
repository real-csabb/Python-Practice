# MY INVENTORY DESCRIPTIONS AND PRICES

# My lovely loveseat.
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

lovely_loveseat_price = 254.00

# My stylish settee.
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

stylish_settee_price = 180.50

# My luxurious lamp.
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

luxurious_lamp_price = 52.15

# You can't escape the tax man.
sales_tax = 0.088 # 8.80% Sales Tax





# MY FIRST CUSTOMER!
customer_one_total = 0
customer_one_itemization = ""

# Customer 0 buys a lovely loveseat!
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Customer 0 buys a luxurious lamp!
customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n\n" + luxurious_lamp_description

# Customer 0 is ready to checkout!
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Customer 0's receipt!
print(f"""                          
                          CUSTOMER 1 TOTAL
CUSTOMER CART
+ ${lovely_loveseat_price} Lovely Loveseat
+ ${luxurious_lamp_price} Luxurious Lamp
  TOTAL ${customer_one_total}
  
                       ------------------------
                          CUSTOMER 1 ITEMS

{customer_one_itemization}""")