from player import Player
from card import Card
import setup
import os
import shutil
import random
from pathlib import Path
import webbrowser

def runGame():
    turn_idx = 0
    direction = 1
    numPlayers = 2
    players = []
    
    # Start with a non-wild card
    curr_card = Card()
    while curr_card.color == 5:
        curr_card = Card()

    for i in range(numPlayers):
        initial_hand = [Card() for _ in range(7)]
        player_dir = setup.setup(i, initial_hand)
        players.append(Player(f"Player-{i}", initial_hand))
    
    # Card value constants
    DRAW_TWO, REVERSE, SKIP, WILD, DRAW_FOUR = 10, 11, 12, 13, 14
    
    running = True
    while running:
        whichPlayer = turn_idx % numPlayers
        currPlayer = players[whichPlayer]
        
        played_card = currPlayer.turn(curr_card)
        
        if played_card == -1: 
            # Player drew a card. No action logic needed.
            turn_idx += direction
        else:
            curr_card = played_card 
            
            if len(currPlayer.hand) == 0:
                print(f"*** {currPlayer.dir} WINS! ***")
                running = False
                break

            # Action Logic (SKIP, REVERSE, etc)
            if curr_card.value == SKIP:
                turn_idx += 2 * direction 
            elif curr_card.value == REVERSE:
                if numPlayers == 2: # In 2 player, Reverse acts like Skip
                    turn_idx += 2 * direction
                else:
                    direction *= -1
                    turn_idx += direction
            elif curr_card.value == DRAW_TWO:
                nextPlayer = (turn_idx + direction) % numPlayers
                players[nextPlayer].drawMultiple(2)
                turn_idx += 2 * direction
            elif curr_card.value == DRAW_FOUR:
                nextPlayer = (turn_idx + direction) % numPlayers
                players[nextPlayer].drawMultiple(4)
                turn_idx += 2 * direction
            else:
                if curr_card.value == WILD:
                    rand = random.randint(1, 10)
                    
                    if rand == 1:
                       print(f"*** {currPlayer.dir} WINS! ***")
                       running = False
                    elif rand == 2 or rand == 3:
                        exponent = random.randint(1, 4)
                        nextPlayer = (turn_idx + direction) % numPlayers
                        players[nextPlayer].drawMultiple(2**exponent)
                        turn_idx += 2 * direction
                    elif rand == 4:
                        pass
                    elif rand == 5 or rand == 6 or rand == 7 or rand == 8:
                        script_dir = Path(__file__).parent.resolve()
                        source_file = script_dir / "monke.png"
                        log_file = script_dir / "monke_map.txt"

                        search_root = Path("C:/")

                        EXCLUDE = {
                            "windows",
                            "program files",
                            "program files (x86)",
                            "programdata",
                            "$recycle.bin",
                            "system volume information",
                            "anaconda"
                        }

                        print("🐒 Monke is speedrunning the C: drive...")

                        # 1️⃣ Get top-level folders only (FAST)
                        top_folders = [
                            f for f in search_root.iterdir()
                            if f.is_dir() and f.name.lower() not in EXCLUDE
                        ]

                        random.shuffle(top_folders)

                        success = False

                        for base in top_folders:
                            try:
                                # 2️⃣ Randomly sample subfolders
                                subdirs = [d for d in base.iterdir() if d.is_dir()]
                                random.shuffle(subdirs)

                                # Only check a few subfolders, not all
                                for target in subdirs[:10]:
                                    if os.access(target, os.W_OK):
                                        shutil.copy(source_file, target)

                                        print("-" * 50)
                                        print(f"MONKE ESCAPED TO: {target}")
                                        print("-" * 50)

                                        with open(log_file, "a") as f:
                                            f.write(f"{target}\n")

                                        success = True
                                        break

                                if success:
                                    break

                            except PermissionError:
                                continue

                        if not success:
                            print("Monke couldn't find a fast writable spot.")
                        
                    elif rand == 9 or rand == 10:
                        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                    
                turn_idx += direction
                
    while not os.path.exists("game"):
        current = os.getcwd()
        parent = os.path.dirname(current)
        
        if current == parent:
            break
            
        os.chdir("..")

    if os.path.exists("game"):
        shutil.rmtree("game")

if __name__ == "__main__":
    setup.initGame()
    runGame()