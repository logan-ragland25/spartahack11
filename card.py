import random

class Card:
    def __init__(self):
        rand = random.randint(1, 108)

        if rand <= 8:
            # Wilds
            self.color = 5
            # 13 is wild, 14 is draw 4
            self.value = random.randint(13, 14)
        elif rand <= (24 + 8):
            # Actions: 10 is draw 2, 11 is reverse, 12 is skip
            self.color = random.randint(1, 4)
            self.value = random.randint(10, 12)
        else:
            # Number: 0-9
            self.color = random.randint(1, 4)
            self.value = random.randint(0, 9)

    def __repr__(self):
        colors = {1: "Red", 2: "Yellow", 3: "Green", 4: "Blue", 5: "Wild"}
        names = {10: "Draw-2", 11: "Reverse", 12: "Skip", 13: "Wild", 14: "Draw-4"}
        name_str = names.get(self.value, str(self.value))
        return f"{colors[self.color]} {name_str}"