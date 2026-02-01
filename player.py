import os
import time
from card import Card
import setup

class Player:
    def __init__(self, name, hand):
        self.hand = hand 
        self.dir = name

    def draw(self):
        new_card = Card()
        self.hand.append(new_card)
        setup.create_card_file(self.dir, new_card)
        print(f"DEBUG: {self.dir} drew {new_card}")
        return -1 

    def drawMultiple(self, count):
        for _ in range(count):
            self.draw()

    def pickColor(self):
        picker_path = os.path.join(self.dir, "CHOOSE_COLOR")
        if not os.path.exists(picker_path): os.mkdir(picker_path)
        
        colors = {1: "Red", 2: "Yellow", 3: "Green", 4: "Blue"}
        options = []
        for c_id, name in colors.items():
            file_path = os.path.join(picker_path, f"DELETE_FOR_{name.upper()}.txt")
            options.append((file_path, c_id, name))
            with open(file_path, 'w') as f: f.write(f"Delete for {name}")

        print(f"WILD! Delete a file in {picker_path}")
        
        chosen_color = None
        while chosen_color is None:
            for path, c_id, name in options:
                if not os.path.exists(path):
                    chosen_color = c_id
                    break
            time.sleep(0.5)

        # Cleanup
        for path, _, _ in options:
            if os.path.exists(path): os.remove(path)
        try: os.rmdir(picker_path)
        except: pass
        return chosen_color

    def turn(self, curr_card):
        print(f"\n--- {self.dir}'s TURN ---")
        print(f"TOP CARD: {curr_card}")
        
        draw_file_path = os.path.join(self.dir, "DELETE_TO_DRAW.txt")
        with open(draw_file_path, 'w') as f: 
            f.write("Delete to draw.")

        while True:
            # 1. Check Draw
            if not os.path.exists(draw_file_path):
                return self.draw()

            # 2. Check Cards
            for card in self.hand:
                color_names = {1: "Red", 2: "Yellow", 3: "Green", 4: "Blue", 5: "Wild"}
                # USE THE HELPER HERE:
                filename = setup.get_card_filename(card)
                path = os.path.join(self.dir, color_names[card.color], filename)

                if not os.path.exists(path):
                    # Validating
                    is_match = (card.color == curr_card.color or 
                                card.value == curr_card.value or 
                                card.color == 5)
                    
                    if is_match:
                        self.hand.remove(card)
                        if os.path.exists(draw_file_path): os.remove(draw_file_path)
                        
                        if card.color == 5:
                            card.color = self.pickColor()
                        return card
                    else:
                        print(f"ILLEGAL MOVE! {card} cannot play on {curr_card}.")
                        setup.create_card_file(self.dir, card) # Restore file
                        if os.path.exists(draw_file_path): os.remove(draw_file_path)
                        return self.draw() # Penalty draw
            
            time.sleep(0.8)