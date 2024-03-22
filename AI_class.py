
class AI:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.held = []

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
