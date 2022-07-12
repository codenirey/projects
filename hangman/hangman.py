import random
import linecache

wordlist =["typer", "names", "guard"]
linenumber = random.randint(1,5757)
word = linecache.getline("hangmanwords.txt",linenumber)
guess = list("_____")
attempts = 5

print("".join(guess))
while True:
    userinput = str(input("The word has 5 letters, try guessing a letter: ")).lower()

    for i in range (len(word)):
        if word[i] == userinput[0]:
            guess[i] = word[i]
    
    if userinput not in word:
        attempts -= 1
        print("That letter is not in the word.")
        print("You have", attempts, "attempts left!")
        
        if attempts == 0:
            print("GAME OVER! The word was " + word)
            break
    
    if "_" not in guess:
        print("You won the game!")
        break

    print("".join(guess))
    