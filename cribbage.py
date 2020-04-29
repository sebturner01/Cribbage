# Author: Sebastian Turner
# Date: 04/29/20
# A representation of the game of Cribbage for two players

#--------------------------
# Init
#--------------------------
from deck import Card, Deck
from typing import Sequence
from random import randint

#--------------------------
# Consts
#--------------------------

BOARD_LEN = 121

#---------------------------
# Classes
#---------------------------

class Player:
    """"The Player class represents a player, their hand, and location on the board"""
    def __init__(self, hand: Sequence[Card], points=0):
        self.hand = hand
        self.points = points

    def discardCards(cards: Sequence[Card]):
        """Removes the given cards from the players hand."""
        for card in cards:
            try:
                self.hand.remove(card)
            except ValueError:
                printDict = {'val': card.val, 'suit': card.suit}
                print("Card %(val)d%(suit)d is not in the players hand" %printDict)

class Board:
    """A representation of the board with players, crib, and count state"""
    def __init__(self, players: Sequence[Player], deck: Deck, crib: list, cutCard: Card):
        self.players = players
        self.deck = Deck()
        self.crib = []
        self.cutCard = None

#-----------------------------
# Functions
#-----------------------------

"""Scoring Funcitons
TODO:
    getRuns
    getFifteens
    unitTests for scoring
    add Checks for play sequence when cutCard is None
"""

def scoreHand(hand: Sequence[Card], cutCard: Card):
    score = 0
    score += getFifteens(hand, cutCard)
    score += getRuns(hand, cutCard)
    score += getMults(hand, cutCard)
    score += getFlush(hand, cutCard)
    return score


def getJackPoint(hand: Sequence[Card], cutCard: Card):
    """Scores for Jack of suit cut.

    If the player hand contains a Jack of the same suit as that of the cut card
    then they will recieve a point. 

    Inputs: 
        hand - The players hand.
        cutCard - The card cut this round.

    Output:
        int - the number of points scored by jack of suit cut this round
    """
    cutSuit = cutCard.suit
    for card in hand:
        if card.val == JACK and card.suit == cutSuit:
            return 1
    return 0


def getFlush(hand: Sequence[Card], cutCard: Card):
    """Scores for flushes. A flush can be four cards of the same suit if those cards
    are all originally in the players hand. If those four cards are present in 
    and the cutCard is also of the same suit then the flush is worth five points.

    Inputs: 
        hand - The players hand
        cutCard - The card cut this round

    Output:
        int - The points scored by flushes in this hand

    """
    cardSuit = -1
    for card in hand:
        if cardSuit == -1:
            cardSuit = card.suit
        elif cardSuit != card.suit:
            return 0
    if cardSuit != cutCard.suit:
        return 4
    return 5


def getMults(hand: Sequence[Card], cutCard: Card):
    """Scores for multiples of cards.
    
    Finds all the multiples of cards in the players hand with the addition of the
    cut card (e.g. pairs, three-of-a-kind, and four-of-a-kind). A pair is worth 2, 
    three-of-a-kind is worth 6, four-of-a-kind 12.

    Inputs: 
        hand - The players hand
        cutCard - The card cut this round

    Output: 
        int - The number of points scored by multiples of one card in this hand plus 
        the cut card

    """
    points = 0
    matched = {}
    for card in hand:
        if matched.get(card) != None:
            matched[cutCard] += 1
        else:
            matched[card] = 0
    if matched.get(cutCard) != None:
            matched[cutCard] += 1
    for card in matched:
        points += matched[card]*(matched[card] + 1)
    return points

def getRuns(hand: Sequence[Card], cutCard: Card):
    """Checks the given hand plus the cut card for runs (e.g. cards of consecutive
    value).

    Input:
        hand - The players hand
        cutCard - The card cut this round
    
    Output:
        int - the number of points scored this round by runs

    """
    points = 0
    return points

def getFifteens(hand: Sequence[Card], cutCard: Card):
    points = 0
    return points


def hasWon(player: Player) -> bool:
    """Checks if the current player has won the game.
    
    A player has one the game if their point total is equal to or exceeds the 
    board length.

    Input:
        player - The player who will be checked

    Output:
        bool - A boolean indicating whether or not the player has won.
    """
    if player.points >= BOARD_LEN:
        return True
    return False


"""Playing Functions
TODO:
    finish 'playPlaySection'
    make 'playRound'
    make 'playGame'
"""

def dealRound(board: Board, dealer: Player)
    """Deals a single round of cribbage (assumes two players)

    Shuffles the deck and deals six cards to each player.

    Input:
        board  - the board for this game.
        dealer - the current dealer for this round. This player is to recieve 
                 cards second.

    """
    deck = board.deck
    deck.shuffle()
    deck.cut(randint(0, DECK_LEN))
    dealtCards = deck.deal(6, 2)
    for hand, player in zip(dealtCards, board.players):
        player.hand = hand

def discardAndCut(board: Board, player1Cards: Sequence[Card], player2Cards: Sequence[Card], cutLoc: int, dealer: Player):
    """Places discard cards in the crib and cuts the deck at the specified location

    Each player is two discard 2 cards which will go into the crib. After the
    crib is established the deck is cut and the resulting top card becomes the
    'cutCard' for the board. 

    Input:
        board - The current Board that the game is being played on
        player1Cards - The first player's cards to be discarded
        player2Cards - The second player's cards to be discarded
        cutLoc - the location the deck is to be cut in.

    """
    board.crib = player1Cards + player2Cards
    board.deck.cutDeck(cutLoc)
    cutCard = board.deck.getTopCard()
    if cutCard.val == JACK:
        dealer.points += 1
    board.cutCard = cutCard
    

def reset(board: Board):
    """Resets the deck for the next round of play

    Takes all cards from the players hands, the crib, and the cut card and 
    returns them to the deck.

    Inputs:
        board - the current Board that the game is being played on
    """
    deck = board.deck

    # Return Player cards
    for player in board.players:
        deck.extend(player.hand)
    
    # Return crib
    deck.extend(board.crib)

    # Return cut card
    deck.append(board.cutCard)


def initGame():
    """Initializes a game of Cribbages

    Initializes a game with two players

    Output:
        board - a board with a deck and 2 players (score intialized to 0)
    """
    players = [Player([]), Player([])]
    deck = Deck()
    return Board(players, deck, [], None)

def playPlaySection(board: Board):
    """Plays the 'play' poriton of the game of cribbage

    Each player in turn plays cards until they both run out. If a player can
    play they must do so. Points are scored for 
    """

def playRound(board: Board, dealer: Player):
    """Plays a single round of cribbage

    Plays through a sinlge round of cribbage which consisting of dealing, discard,
    play, scoring hands, and scoring the crib. If at any point scoring interval an
    induvidual wins the game is over.

    Input:
        board - the current Board the game is being played on
        dealer- the player who is the current dealer and who recieves the crib
    """
    dealRound(board)
    # Discard and cut
    # Play
    # Count hands
    [player.score += scoreHand(play.hand, cutCard) for player in board.players]    
    # Dealer counts crib
    dealer.score += scoreHand(board.crib, cutCard)
    # Reset

#-------------------------------
# Tests
#-------------------------------

def unitTests():
    players = [Player([], 0), Player([], 0)]
    board = Board(players, [], None)