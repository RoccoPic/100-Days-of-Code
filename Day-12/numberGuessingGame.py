from random import randint

print("Welcome to the Number GuessingGame!")
print("I'm thinkin of a number between 1 and 100.")

#select hard, you get 5 guesses/ select easy you get 10
def guessGame():
    number2Guess = randint(1,100)
    guessed = False
    global lives
    lives = setLives()
    #game begins
    while guessed == False: 
        print(f"You have {lives} attempts remaining to guess the number.") #you have x Lives and you can guess
        guessed = howClose(int(input("Make a guess: ")),number2Guess) #calls our function, if true we get out and we it
    again = input("Would you like to play again? 'y' or 'n': ")
    if again == 'y':
        guessGame()
    else:
        print("Game over")

def setLives():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = 10
        return lives
    elif difficulty == 'hard':
        lives = 5
        return lives
    else:
        guessGame()

def howClose(guess,hiddenNumber):
    global lives
    if guess == hiddenNumber:
        print(f"Congratulations the answer was {hiddenNumber}")
        return True
    elif guess < hiddenNumber:
        print("Too low")
        lives-=1
        return False
    elif guess > hiddenNumber:
        print("Too high")
        lives-=1
        return False


guessGame()