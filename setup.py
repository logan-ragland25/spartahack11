import os

def initGame():
    if not os.path.exists("game"):
        os.mkdir("game")
    os.chdir("game")

def get_card_filename(card):
    """Generates the exact filename string used for tracking."""
    names = {10: "Draw-2", 11: "Reverse", 12: "Skip", 13: "Wild", 14: "Draw-4"}
    name_str = names.get(card.value, str(card.value))
    return f"{name_str}_{id(card)}"

def create_card_file(player_folder, card):
    colors = {1: "Red", 2: "Yellow", 3: "Green", 4: "Blue", 5: "Wild"}
    color_name = colors[card.color]
    
    filename = get_card_filename(card)
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

    for card in initial_hand:
        create_card_file(player_folder, card)
        
    return player_folder