import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choises = {"player": player_choice, "computer": computer_choice}

    return choises

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It'S a tie!"
    
    elif player == "rock":  
        if computer == "scissors":
            return "Rock smashes scissors! You Win!"
        else:
            return "Paper covers rock! You Lose."
        
    elif player == "paper":  
        if computer == "rock":
            return "Paper covers rock! You Win!"
        else:
            return "Scissors cuts paper! You Lose."
        
    elif player == "scissors":  
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock smashes scissors! You Lose."

choises = get_choices()
result = check_win(choises["player"], choises["computer"])
print(result)
