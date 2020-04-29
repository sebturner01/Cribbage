# Author: Sebastian Turner
# Date: 04/29/20
# A representation of the game of Cribbage for two players

#--------------------------
# Init
#--------------------------
import deck

#--------------------------
# Consts
#--------------------------

BOARD_LEN = 121

#---------------------------
# Classes
#---------------------------

class Player:
    """"The Player class represents a player, their hand, and location on the board"""
    def __init__(self, hand: list[Cards], loc):
        self.hand = hand
        loc = 0

    def discardCards(cards: list[Cards]):
        """Removes the given cards from the players hand."""
        for card in cards:
            try:
                self.hand.remove(card)
            except ValueError:
                printDict = {'val': card.val, 'suit': card.suit}
                print("Card %(val)d%(suit)d is not in the players hand" %printDict)
                

class Board:
    """A representation of the board with players, crib, and count state"""
    def __init__(self, players: list, crib: list, cutCard: Card):
        self.players = players
        self.crib = []
        self.cutCard = None

def scoreHand(hand: list[Card], cutCard: Card):
    score = 0
    score += getFifteens(hand, cutCard)
    score += getRuns(hand, cutCard)
    score += getMults(hand, cutCard)
    score += getFlush(hand, cutCard)
    return score

"""
Scores for Jack of suit cut. 

Inputs:

hand - The players hand
cutCard - The card cut this round
"""
def getJackPoint(hand: list[Card], cutCard: Card):
    cutSuit = cutCard.suit
    for card in hand:
        if card.val == JACK and card.suit == cutSuit:
            return 1
    return 0

"""
Scores for flushes. A flush can be four cards of the same suit if those cards
are all originally in the players hand. If those four cards are present in 
and the cutCard is also of the same suit then the flush is worth five points

Inputs:

hand - The players hand
cutCard - The card cut this round
"""
def getFlush(hand: list[Card], cutCard: Card):
    lastSuit = -1
    for card in hand:
        if lastSuit == -1:
            lastSuit = card.suit
        elif lastSuit != card.suit:
            return 0
    if lastSuit != cutCard.suit:
        return 4
    return 5

def getMults(hand: list[Card], cutCard: Card):

def getRuns(hand: list[Card], cutCard: Card):

def getFifteens(hand: list[Card], cutCard: Card):


