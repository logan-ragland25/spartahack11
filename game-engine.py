from player import Player
from card import Card
import setup

def runGame():
    turn = 0
    direction = 1
    numPlayers = 2
    players = []
    running = True
    curr = Card

    # Create each player, and assign them a card directory
    for i in range(numPlayers):
        newPlayer = Player(setup.setup(i))
        players.append(newPlayer)
    
    
    DRAW_TWO    =   10
    REVERSE     =   11
    SKIP        =   12
    WILD        =   13
    DRAW_FOUR   =   14
    
    while running:
        
        
        
        # Number for current player
        whichPlayer = turn % numPlayers

        # Object for current player
        currPlayer = players[whichPlayer]
        curr = currPlayer.turn(curr)
        
        # If wild card
        if curr.value >= WILD:
            turn += direction
            #Pick color()       ------------------------------------------ STILL NEEDS DONE
            # If draw four, make next player draw and skip their turn
            if curr.value == DRAW_FOUR:
                turn += direction
                players[whichPlayer + direction].drawMultiple(4)
        
        # If skip card
        elif curr.value == SKIP:
            turn += 2 * direction 
        
        # If reverse card
        elif curr.value == REVERSE:
            direction *= -1
            turn += direction
            
        # If draw two card
        elif curr.value == DRAW_TWO:
            #draw 2 card
            turn += 2 * direction
            players[whichPlayer + direction].drawMultiple(2)
            
        # If normal card
        else:
            turn += direction

        if currPlayer.hand.size() == 0:
            print(f"Game Over: player {whichPlayer} won!")
            running = False
        

if __name__ == "__main__":
    setup.initGame()
    runGame()
    