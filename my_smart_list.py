my_smart_list = []

print('\nHello there! While the program is running, type "Exit" to end it.\n')

while True:
    i = input("Enter something! Anything!: ")
    if i == "Exit" or i == "exit":
        break
    """elif function that checks for "call" and
            then gets the index number provided.
    """
    """ elif function that checks for "Remove" and
            then removes index number or value provided.
    """
    else:
        my_smart_list.append(i)
        print(my_smart_list)