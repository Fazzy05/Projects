import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]
while True:
    user_input = input("Please Enter Rock/Paper/Scissor or q to Quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == 'rock' and computer_pick == 'scissor':
        print("You Win!")
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You Win!")
        user_wins += 1
    elif user_input == 'scissor' and computer_pick == 'paper':
        print("You Win!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a Draw!")
        user_wins += 1
        computer_wins += 1
    else:
        print("You Lost")
        computer_wins += 1
print("You Won", user_wins, "times.")
print("Computer Won", computer_wins, "times.")