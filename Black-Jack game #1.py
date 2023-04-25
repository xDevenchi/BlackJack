import random #picks a random variable for the cards 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

#creating card class. This creates our cards/objects

class Card:

    def __init__(self, suit, rank): #Makes the object. Self refers to the card
        self.suit = suit #Describes object value
        self.rank = rank #Describes object value
    
    def __str__(self):
        return self.rank + ' of ' + self.suit #says what specific card 

