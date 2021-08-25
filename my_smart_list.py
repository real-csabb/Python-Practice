my_smart_list = []

print('\nHello there! While the program is running, type "Exit" to end it.\n')

while True:
    i = input("Enter something! Anything!: ")
    if i == "Exit" or i == "exit":
        break
    else:
        my_smart_list.append(i)
        print(my_smart_list)