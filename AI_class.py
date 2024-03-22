

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

    def check_yahtzee(self):
        same_number = 0
        for die in self.hand:
            if die == self.hand[0]:
                same_number += 1
        if same_number == 5:
            print("YAHTZEE!")
        else:
            print("nothing.")


names = ['Ughene', 'Alpbert', 'Kharleigh', 'Catelenhn']
