# Number Guessing Game using Python

import random

# Allow the user to play multiple rounds
while True:

    # Computer randomly selects a number between 1 and 100
    secret_number = random.randint(1, 100)

    # Keep track of the number of attempts
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    # Keep asking until the user guesses correctly
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Give hints based on the user's guess
            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("Correct! You guessed the number.")
                print("Number of attempts:", attempts)
                break

        # Handle invalid input
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask whether the user wants another round
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
    