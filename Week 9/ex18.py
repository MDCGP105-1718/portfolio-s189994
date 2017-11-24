import random

#we put the main class on top
class Card(object):
#data attributes are other objects that make up the class itself

    values = ["Ace", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
#we put the constructor for a class - "__init__". We create an instance of our object.
    def __init__ (self,suit,value):
        self.suit = suit
        self.value = value
#the string returns the representation of the object
    def __str__(self):
        return Card.values[self.value] + ' of ' + Card.suits[self.suit]

    def __str__(self):
        return self.get_value() + ' of ' + self.get_suit()

    __repr__ = __str__

def get_card_shuffle(card):
    
   return card.shuffle

card = Card(0, 5)
print(card)
#we introduce another class (different from the other one. It also concludes suits and values.)
class Deck(object):

   def __init__(self):
        self.cards = []
        self.current_card = 0
        for suit in range(4):
            for value in range(13):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        self.cards.sort(key=get_card_shuffle)
        self.current_card = 0

    def deal_hand(self, hand, number_to_deal):
        if self.current_card + number_to_deal >= len(self.cards):
            return

        # loop through the deck for number_to_deal times
        for i in range(self.current_card, self.current_card + number_to_deal):
            # each loop will call hand.add_card
            hand.add_card(self.cards[i])
            self.current_card += 1

deck = Deck()
deck.shuffle()

class Hand(Deck):

def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        aces = 0
        value = 0

hand = Hand()
deck.deal_hand(hand, 5)

hand2 = Hand()
deck.deal_hand(hand2, 5)

print(hand.cards)
print(hand2.cards)

