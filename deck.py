# Author: Sebastian Turner 
# Date: 04/29/20
# A represenation of a deck of cards with the ace as the low card (1)


#--------------------
# Imports
#--------------------

from random import shuffle

#---------------------
# Constants
#---------------------

DECK_LEN = 52

suits = [n for n in range(4)]
CLUBS = 0
DIAMONDS = 1
HEARTS = 2
SPADES = 4

# Ace is low in this implementation of the deck
cardValues = [n for n in range(1, 13)]
JACK = 11
QUEEN = 12
KING = 13
ACE = 1

"""
TODO:
    Fix Documentation to PEP-8
"""

class Card:
    """The Card class represents a sinlge card in a deck of cards"""
    def __init__(self, suit: int = 0, val: int = ACE):
        self.suit = suit
        self.val = val

class Deck:
    """The deck class represents a single deck of cards. The top of this deck is at 0"""
    def __init__(self):
        self.deck = self.makeDeck()

    def makeDeck(self):
        """Makes a new deck of cards of length 52 in order"""
        cards = []
        for suit in suits:
            for val in cardValues:
                newCard = Card(suit, val)
                cards.append(newCard)
        return cards
    
    def shuffle(self):
        """Shuffles a deck of cards in place using random.shuffle()"""
        shuffle(self.deck)

    def getTopCard(self) -> Card:
        """Returns the top card from the deck"""
        return self.deck.pop(0)
    
    def deal(self, nCards: int, nPlayers: int):
        """Deals nCards to nPlayers. If this value is larger than the number of cards in the deck then cards will be dealt to the end of the deck. Returns a dictionary of 'hands' for each player"""
        hands = {}
        for n in range(nPlayers):
            hands[n] = []
        card = 0
        while card < nCards:
            for player in range(nCards):
                if self.deck:
                    hands[player].append(self.getTopCard)
            card += 1
    def addCards(self, cards: list):
        """Adds the given list of cards to the deck"""
        self.deck += cards
    
    def cutDeck(self, cutLoc: int):
        """Cuts the deck such that the cards from cutLoc to the end of the deck
        are placed ontop of the card from 0 to the cutLoc"""
        self.deck = self.deck[cutLoc:] + self.deck[:cutLoc]

    