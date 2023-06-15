from random import randint
from logo import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def choose_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Please, try to choose difficulty again")


def guess_number(guessed_num, random_num, attempts):
    if guessed_num > random_num:
        print("Too high.")
        print("Guess again.")
        return attempts - 1
    elif guessed_num < random_num:
        print("Too low.")
        print("Guess again.")
        return attempts - 1
    elif guessed_num == random_num:
        print(f"You got it! The answer was {guessed_num}.")


def guessing_number_game():
    random_num = randint(1, 100)
    print(random_num)
    attempts = choose_difficulty()
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_num = int(input("Make a guess: "))
        attempts = guess_number(guessed_num, random_num, attempts)

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            break
        elif guessed_num == random_num:
            break

guessing_number_game()

