# Author: Sebastian Turner
# Date: 04/29/20
# A representation of the game of Cribbage

#---------------------------
# Classes
#---------------------------

class Player:
    """"The Player class represents a player, their hand, and location on the board"""
    def __init__(self, s):
        self.hand = {}