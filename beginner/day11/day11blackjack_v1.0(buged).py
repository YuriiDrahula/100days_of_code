from random import randint
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add_card(cards_list):
    cards_list.append(cards[randint(0, 12)])


def check_blackjack(user_cards, computer_cards):
    if user_cards == [11, 10] or user_cards == [10, 11]:
        print("User has a blackjack! User wins!")
        stop_program()
    elif computer_cards == [11, 10] or computer_cards == [10, 11]:
        print("Computer has a blackjack! Computer wins!")
        stop_program()


def check_user_hand(user_cards):
    if sum(user_cards) > 21:
        for i in range(len(user_cards)):
            if user_cards[i] == 11:
                user_cards[i] = 1
                if sum(user_cards) > 21:
                    print("Computer wins")
                    stop_program()
            else:
                print("Computer wins")
                stop_program()
    else:
        choice = input("Do you want to get another card? Type 'y' or 'n': ")
        if choice == 'y':
            add_card(user_cards)
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            check_user_hand(user_cards)
        else:
            check_winner(user_cards, computer_cards)


def check_computer_hand(computer_cards):
    while sum(computer_cards) < 17:
        add_card(computer_cards)
    if sum(computer_cards) > 21:
        print_total_score()
        print("User wins")
        stop_program()


def check_winner(user_cards, computer_cards):
    if sum(user_cards) > sum(computer_cards):
        print_total_score()
        print("You win!")
    elif sum(user_cards) < sum(computer_cards):
        print_total_score()
        print("Computer wins!")
    else:
        print_total_score()
        print("Draw")


def stop_program():
    global run_program
    run_program = False


def print_total_score():
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")


run_program = True
while run_program:
    user_cards = [cards[randint(0, 12)], cards[randint(0, 12)]]
    computer_cards = [cards[randint(0, 12)], cards[randint(0, 12)]]

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "n":
        stop_program()
    else:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        check_blackjack(user_cards, computer_cards)
        check_user_hand(user_cards)

        check_computer_hand(computer_cards)
        check_winner(user_cards, computer_cards)