# IMPORTS
import random as r

# VARIABLES
name = input("\nEnter a name: ")
question = input("Ask a question: ")
answer = ""
random_number = r.randint(1,10)
# print(random_number)

# ALGORITHM
if name == "" or question == "":
  if name == "":
    print("Please insert an name.")
  else:
    print("The fabric of reality is at risk. Please ask an question.")
elif "Waffle Guy" in question:
    print(f"\n{name} asks: {question}", end="\n")
    print("Magic 8-Ball's answer: It is decidedly so.")
else:
  print(f"\n{name} asks: {question}", end="\n")
  print("Magic 8-Ball's answer: ", end="")
  if random_number == 1:
    print("Yes, definitely.")
  elif random_number == 2:
    print("It is decidedly so.")
  elif random_number == 3:
    print("Without a doubt.")
  elif random_number == 4:
    print("Reply hazy, try again.")
  elif random_number == 5:
    print("Ask again later.")
  elif random_number == 6:
    print("Better not tell you now.")
  elif random_number == 7:
    print("My sources say no.")
  elif random_number == 8:
    print("Outlook not so good.")
  elif random_number == 9:
    print("Very doubtful.")
  elif random_number == 10:
    print("Signs point to yes.")
  else:
    print("An error has occurred.")