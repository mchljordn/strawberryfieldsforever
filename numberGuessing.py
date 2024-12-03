import random

numToGuess = random.randint(1, 1000)
numOfGuesses = 0
guess = -1

print("Guess a number between 1 and 1000")

while guess != numToGuess:
    try:
        guess = int(input("Enter your guess: "))
        numOfGuesses += 1
        if guess > numToGuess:
            print("Too high!")
        elif guess < numToGuess:
            print("Too low!")
        else:
            print("You got it!")
            print("It took you", numOfGuesses, "guesses.")
            if numOfGuesses == 1:
                print("You're a mind reader!")
            elif numOfGuesses < 10:
                print("Either you know the secret or you got lucky!")
            elif numOfGuesses > 10:
                print("You fuckin stoopid")
    except ValueError:
        print("Please enter a valid integer.")