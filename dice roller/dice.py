import random

def roll():
    number = random.randint(1,6)
    print("You got", str(number) + "!")

while True:
    yeno = input("Would you like to roll the dice? (y/n): ")
    if yeno == "y":
        roll()
    if yeno =="n":
        print("Have a nice day!")
        break