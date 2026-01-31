import os

def initGame():
    if not os.path.exists("game"):
        os.mkdir("game")
    os.chdir("game")

def setup(playerNumber):
    player_folder = (f"Player-{playerNumber}")
        
    os.mkdir(player_folder)
    os.chdir(player_folder)
    
    colors = ["Wild", "Red", "Yellow", "Green", "Blue"]
    for color in colors:
        os.mkdir(color)

        if color == "Wild":
            os.chdir("Wild")
            os.mkdir("colorPicker")
            os.chdir("..\..")
    
    os.chdir("..")
    return (player_folder)
    