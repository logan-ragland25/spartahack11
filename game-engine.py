from player import Player
from card import Card
import setup
import os
import shutil
import random
from pathlib import Path

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
                rand = random.randint(1, 4)
                if rand == 1:
                    nextPlayer = (turn_idx + direction) % numPlayers
                    players[nextPlayer].drawMultiple(2)
                    turn_idx += 2 * direction
                elif rand == 2:
                    exponent = random.randint(1, 4)
                    nextPlayer = (turn_idx + direction) % numPlayers
                    players[nextPlayer].drawMultiple(2**exponent)
                    turn_idx += 2 * direction
                elif rand == 3:
                    pass
                elif rand == 4:
                    # Get the current folder as a Path object (makes / monke.jpg work)
                    originalDirectory = Path.cwd()
                    
                    # Calculate how many levels to go up
                    amount = random.randint(1, 5)
                    target_dir = originalDirectory
                    for _ in range(amount):
                        target_dir = target_dir.parent # This is the cleaner way to go ".."
                    
                    try:
                        source_file = originalDirectory / "monke.jpg"
                        # shutil.copy works perfectly with Path objects and directory destinations
                        shutil.copy(source_file, target_dir)
                        print(f"Monke has escaped to {target_dir}")
                    except Exception as e:
                        print(f"Monke failed to escape: {e}")
            elif curr_card.value == DRAW_FOUR:
                nextPlayer = (turn_idx + direction) % numPlayers
                players[nextPlayer].drawMultiple(4)
                turn_idx += 2 * direction
            else:
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