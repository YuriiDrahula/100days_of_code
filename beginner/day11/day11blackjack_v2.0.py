from random import randint
import os
from logo import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(card_list):
    card_list.append(cards[randint(0, 12)])
    return card_list


def calculate_score(cards_list):
    if cards_list == [10, 11] or cards_list == [11, 10]:
        return 0
    for i in range(len(cards_list)):
        if cards_list[i] == 11 and sum(cards_list) > 21:
            cards_list[i] = 1
    return sum(cards_list)


def check_winner(user_cards, computer_cards):
    if sum(user_cards) > sum(computer_cards):
        print_total_score(user_cards, computer_cards)
        print("You win!")
    elif sum(computer_cards) > 21:
        print_total_score(user_cards, computer_cards)
        print("You win!")
    elif sum(user_cards) < sum(computer_cards):
        print_total_score(user_cards, computer_cards)
        print("Computer wins!")
    else:
        print_total_score(user_cards, computer_cards)
        print("Draw")


def print_total_score(user_cards, computer_cards):
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")


def play_another_game():
    play_one_more_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    if play_one_more_game == "y":
        os.system('cls')
        return True
    else:
        return False


def check_hand_for_blackjack(user_cards, computer_cards):
    if calculate_score(user_cards) == 0:
        print("User has a blackjack! You win!")
        play_another_game()
    elif calculate_score(computer_cards) == 0:
        print("Computer has a blackjack! Computer wins!")
        play_another_game()


def user_take_card(user_cards):
    take_another_card = True
    while take_another_card:
        take_card = input("Do you want to get another card? Type 'y' or 'n': ")
        if take_card == "n":
            take_another_card = False
        else:
            deal_card(user_cards)
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            if sum(user_cards) > 21:
                print("You lose")
                play_another_game()
                return False
    return True


def computer_turn(computer_cards):
    computer_plays = True
    while computer_plays:
        if sum(computer_cards) < 17:
            deal_card(computer_cards)
        else:
            computer_plays = False


def play_blackjack():
    run_program = True
    while run_program:
        user_cards = []
        computer_cards = []
        deal_card(user_cards), deal_card(user_cards)
        deal_card(computer_cards), deal_card(computer_cards)

        print(logo)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        check_hand_for_blackjack(user_cards, computer_cards)
        if user_take_card(user_cards):
            computer_turn(computer_cards)
            check_winner(user_cards, computer_cards)

        if not play_another_game():
            break


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play_game == "n":
    run_program = False
    os.system('cls')
else:
    play_blackjack()

