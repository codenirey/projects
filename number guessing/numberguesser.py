import random

randomnum = random.randint(1,100)
trys = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100 :--: "))
    except ValueError:
        print("Oops, that is not a number! Try again.")
        continue
    if guess == randomnum:
        trys += 1
        print("You got it! It was", str(randomnum), "and it took you", str(trys), "attempts!")
        break

    if guess > randomnum:
        trys += 1
        print("Lower!")

    if guess < randomnum:
        trys += 1
        print("Higher!")