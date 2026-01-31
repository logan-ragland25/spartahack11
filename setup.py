import os

def initGame():
    if not os.path.exists("game"):
        os.mkdir("game")
    os.chdir("game")

def create_card_file(player_folder, card):
    """Creates a physical file for a card."""
    colors = {1: "Red", 2: "Yellow", 3: "Green", 4: "Blue", 5: "Wild"}
    color_name = colors[card.color]
    
    # Use the card's memory ID to ensure the filename is unique
    if(card.value < 10):
        filename = f"{card.value}_{id(card)}.txt"
    else:
        name = ''
        if card.value == 10:
            name = "Draw-2"
        elif card.value == 11:
            name = "Reverse"
        elif card.value == 12:
            name = "Skip"
        elif card.value == 13:
            name = "Wild"
        else:
            name = "Draw-4"
        filename = f"{name}_{id(card)}.txt"
    filepath = os.path.join(player_folder, color_name, filename)
    
    with open(filepath, 'w') as f:
        f.write(f"Color: {color_name}\nValue: {card.value}\nID: {id(card)}")
    return filepath

def setup(playerNumber, initial_hand):
    player_folder = f"Player-{playerNumber}"
    if not os.path.exists(player_folder):
        os.mkdir(player_folder)
    
    colors = ["Red", "Yellow", "Green", "Blue", "Wild"]
    for color in colors:
        path = os.path.join(player_folder, color)
        if not os.path.exists(path):
            os.mkdir(path)

    # Create files for the initial 7 cards
    for card in initial_hand:
        create_card_file(player_folder, card)
        
    return player_folder