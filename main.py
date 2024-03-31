import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choises = {"player": player_choice, "computer": computer_choice}

    return choises

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It'S a tie!"

check_win("rock", "paper")
