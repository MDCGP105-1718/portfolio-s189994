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

card = Card(0, 5)
print(card)
#we introduce another class (different from the other one. It also concludes suits and values.)
class Deck(object):

    def __init__(self):
        self.deck=[] #we put an empty value because that way (from the next 4 lines) we will add cards in it (randomly)

        for suit in range(4):
            for value in range(0, 13):
                card = Card(suit, value) #we define card
                self.deck.append(card)

    def shuffle(self):
        import random

        number_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

deck = Deck()
card = deck.deck[random.randint(0,51)]
print(card)

class Hand(Deck):

    def add_card(self, card):
        self.hand.append(card)
        return self.hand

    def get_value(self):
        aces = 0
        value = 0
