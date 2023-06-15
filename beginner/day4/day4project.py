import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("Enter 1 for Rock, 2 for Paper or 3 for scissors\n"))
print("User choose")

if user_choice >= 4 or user_choice <= 0:
    print("You've entered wrong number, reload the game and try again")
else:
    print(game_images[user_choice - 1])

    computer_choice = random.randint(1, 3)
    print("Computer choose")
    print(game_images[computer_choice - 1])

    if user_choice == computer_choice:
        print("Draw!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("You've lost!")

