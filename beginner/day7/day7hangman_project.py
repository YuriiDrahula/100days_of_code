import random
from hangman_art import stages, logo
from hangman_word_list import word_list

print(logo)
chosen_word = random.choice(word_list)


guessed_word = []
for letter in chosen_word:
    guessed_word.append("_")

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    i = 0

    if guess in guessed_word:
        print(f"You've already guessed the letter - {guess}")
        continue

    for letter in chosen_word:
        if letter == guess:
            print(f"You've guessed the letter - {letter}. Keep going!")
            guessed_word[i] = letter
        i += 1

    if guess not in chosen_word:
        print(f"You choose letter - {guess}. It's not in the word, you've lost 1 life")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("Ooops, you're out of lives and lost the game!")

    your_word = "".join(guessed_word)
    if your_word == chosen_word:
        end_of_game = True
        print("Congratulations, you win the game!")

    print(your_word)
