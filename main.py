def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    computer_choice = "paper"
    choises = {"player": player_choice, "computer": computer_choice}

    return choises

choises = get_choices()
print(choises)
