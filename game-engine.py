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
                    rand = 5
                    print(rand)
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
                        # 1. Setup paths
                        script_dir = Path(__file__).parent.resolve()
                        source_file = script_dir / "monke.jpg"
                        log_file = script_dir / "monke_map.txt"

                        # Search your User folder (C:\Users\Logan)
                        search_root = Path.home()
                        potential_spots = []

                        print("🐒 Monke is searching your entire user directory for a spot...")

                        # 2. Collect a LARGE list of folders
                        for root, dirs, files in os.walk(search_root):
                            # Filter out Anaconda and hidden folders to keep it interesting
                            dirs[:] = [d for d in dirs if not d.startswith('.') and 'anaconda' not in d.lower()]
                            
                            for name in dirs:
                                full_path = Path(root) / name
                                potential_spots.append(full_path)
                            
                            # Increase the limit so we see more than just the first few folders
                            if len(potential_spots) > 1000:
                                break

                        # 3. SHUFFLE and Verify
                        # This ensures we don't just pick the first ones found
                        random.shuffle(potential_spots)

                        success = False
                        for target in potential_spots:
                            # Check write access one by one until one works
                            if os.access(target, os.W_OK):
                                try:
                                    shutil.copy(source_file, target)
                                    
                                    # Print feedback
                                    print("-" * 50)
                                    print(f"✅ MONKE ESCAPED TO: {target}")
                                    print("-" * 50)

                                    # Log for later
                                    with open(log_file, "a") as f:
                                        f.write(f"{target}\n")
                                    
                                    success = True
                                    break # Exit once we successfully hide one monke
                                except Exception:
                                    continue

                        if not success:
                            print("❌ Monke couldn't find a spot outside of restricted areas.")
                        
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