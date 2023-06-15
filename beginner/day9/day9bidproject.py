import os
from logo import logo

print(logo)
bid_dict = {}


def bid_func(bidder_name, sum_of_bid):
    bid_dict[bidder_name] = sum_of_bid


def choose_winner():
    max_bid = 0
    winner = ""
    for bidder in bid_dict:
        if bid_dict[bidder] > max_bid:
            max_bid = bid_dict[bidder]
            winner = bidder
    print(f"The winner is {winner}, with the bid ${max_bid}")


run_program = True
while run_program:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_func(name, bid)

    choice = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if choice == "no":
        run_program = False
        choose_winner()
    else:
        os.system("cls")