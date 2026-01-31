from player import Player
from card import Card
import setup
import os

def runGame():
    turn_idx = 0
    direction = 1
    numPlayers = 2
    players = []
    
    # Start the game with a random card on the table
    curr_card = Card()
    while curr_card.color == 5: # Ensure the game doesn't start on a wild
        curr_card = Card()

    # Create each player and their initial hand/files
    for i in range(numPlayers):
        initial_hand = [Card() for _ in range(7)]
        player_dir = setup.setup(i, initial_hand)
        players.append(Player(f"Player-{i}", initial_hand))
    
    # Constants
    DRAW_TWO, REVERSE, SKIP, WILD, DRAW_FOUR = 10, 11, 12, 13, 14
    
    running = True
    while running:
        whichPlayer = turn_idx % numPlayers
        currPlayer = players[whichPlayer]
        
        # turn() now waits for file deletion and returns the Card object or -1
        played_card = currPlayer.turn(curr_card)
        
        if played_card == -1:
            # Player drew a card, move to next turn
            turn_idx += direction
        else:
            # Player successfully played a card
            curr_card = played_card
            
            # Check Win Condition
            if len(currPlayer.hand) == 0:
                print(f"GAME OVER: {currPlayer.dir} wins!")
                running = False
                break

            # Handle Special Card Logic
            if curr_card.value == SKIP:
                turn_idx += 2 * direction 
            elif curr_card.value == REVERSE:
                direction *= -1
                turn_idx += direction
            elif curr_card.value == DRAW_TWO:
                nextPlayer = (turn_idx + direction) % numPlayers
                players[nextPlayer].drawMultiple(2)
                turn_idx += 2 * direction # Skip their turn
            elif curr_card.value == WILD or curr_card.value == DRAW_FOUR:
                # Simple Wild Logic: For now, it stays the color of the Wild card 
                # (which is randomly assigned 1-4 in a full game implementation)
                if curr_card.value == DRAW_FOUR:
                    nextPlayer = (turn_idx + direction) % numPlayers
                    players[nextPlayer].drawMultiple(4)
                    turn_idx += 2 * direction
                else:
                    turn_idx += direction
            else:
                turn_idx += direction

if __name__ == "__main__":
    setup.initGame()
    runGame()