# Number Guessing Game Objectives:
#   Include an ASCII art logo.
#   Allow the player to submit a guess for a number between 1 and 100.
#   Check user's guess against actual answer. Print "Too high." Or "Too low." Depending on the user's answer.
#   If they got the answer correct, show the actual answer to the player.
#   Track the number of turns remaining.
#   If they run out of turns, provide feedback to the player.
#   Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random


def clear():  # Prints 50 blank lines
    print("\n" * 50)


def play_game():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 101)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.\n")
            return
        elif guess < number:
            print("Too low\nGuess again\n")
        else:
            print("Too high\nGuess again\n")
        attempts -= 1
    return


#######################################

play_again = 'y'

while play_again == "y":
    play_game()
    play_again = input("Type 'y' to play again 'n' to exit: ")

print("******** Thank you ********")
