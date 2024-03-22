import random


class AI:
    def __init__(self, name):
        self.name = name
        self.hand = [0, 0, 0, 0, 0]
        self.held = []
        self.scorecard = {
            "Ones": None,
            "Twos": None,
            "Threes": None,
            "Fours": None,
            "Fives": None,
            "Sixes": None,
            "Three of a Kind": None,
            "Four of a Kind": None,
            "Full House": None,
            "Small Straight": None,
            "Large Straight": None,
            "Yahtzee": None,
            "Chance": None
        }

    def roll_die(self):
        """Lets the AI roll the die"""
        for die in range(0, 5):
            self.hand[die] = random.randint(1, 6)

    def check_yahtzee(self):
        """Allows AI to check for a yahtzee after rolling"""
        same_number = 0
        for die in self.hand:
            if die == self.hand[0]:
                same_number += 1
        if same_number == 5:
            print("YAHTZEE!")
        else:
            print("nothing.")


names = ['Ughene', 'Alpbert', 'Kharleigh', 'Catelenhn']

ughene = AI('Ughene')

ughene.roll_die()
print(ughene.hand)
ughene.check_yahtzee()
