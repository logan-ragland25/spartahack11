import os
import time
from card import Card
import setup

class Player:
    def __init__(self, name, hand):
        self.hand = hand # List of Card objects
        self.dir = name

    def draw(self):
        new_card = Card()
        self.hand.append(new_card)
        setup.create_card_file(self.dir, new_card)
        print(f"{self.dir} drew a card.")
        return -1

    def drawMultiple(self, count):
        for _ in range(count):
            self.draw()

    def turn(self, curr_card):
        print(f"\n{'='*20}")
        print(f"TURN: {self.dir}")
        print(f"TOP CARD: {curr_card}")
        print(f"{'='*20}")
        print("INSTRUCTIONS: Delete a file in your folder to play that card.")
        
        # Create a 'DRAW_CARD.txt' file that the user can delete to draw
        draw_file_path = os.path.join(self.dir, "DELETE_TO_DRAW.txt")
        with open(draw_file_path, 'w') as f: f.write("Delete this to draw a card.")

        while True:
            # 1. Check if the user opted to draw
            if not os.path.exists(draw_file_path):
                return self.draw()

            # 2. Check if a card file was deleted
            for card in self.hand:
                colors = {1: "Red", 2: "Yellow", 3: "Green", 4: "Blue", 5: "Wild"}
                filename = f"{card.value}_{id(card)}.txt"
                path = os.path.join(self.dir, colors[card.color], filename)

                if not os.path.exists(path):
                    # User deleted this file! Check if it's valid.
                    if (card.color == curr_card.color or 
                        card.value == curr_card.value or 
                        card.color == 5):
                        
                        print(f"Validated: {card} played.")
                        self.hand.remove(card)
                        # Clean up the draw file before ending turn
                        if os.path.exists(draw_file_path): os.remove(draw_file_path)
                        return card
                    else:
                        print(f"INVALID MOVE: {card} cannot be played on {curr_card}!")
                        print("Restoring file... You must draw a penalty card.")
                        setup.create_card_file(self.dir, card)
                        if os.path.exists(draw_file_path): os.remove(draw_file_path)
                        return self.draw()
            
            time.sleep(1) # Wait 1 second before checking again