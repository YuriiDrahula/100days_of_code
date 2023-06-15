from data import data
from logo import logo, vs
from random import choice
import os


def compare_followers(followers_a, followers_b):
    if followers_a["follower_count"] > followers_b["follower_count"]:
        os.system('cls')
        return True
    else:
        return False


def game_board(winner, loser, score):
    score += 1
    print(logo)
    print(f"You're right! Current score: {score}")
    loser = choice(data)
    print(f"Compare A: {winner['name']}, a {winner['description']}, from {winner['country']}.")
    print(vs)
    print(f"Against B: {loser['name']}, a {loser['description']}, from {loser['country']}.")
    return score


score = 0
def play_game():
    global score
    account_a = choice(data)
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)

    print(logo)
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
    keep_playing = True
    while keep_playing:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choice == "A" and compare_followers(account_a, account_b) == True:
            score = game_board(account_a, account_b, score)
        elif user_choice == "B" and compare_followers(account_b, account_a) == True:
            score = game_board(account_b, account_a, score)
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            keep_playing = False


play_game()
