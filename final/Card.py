# Name: Marcus Gee
# CMS cluster login name: mcgee
#
# CS 1 Final exam, 2017
#

'''
This module has functions and classes representing playing cards 
and decks of cards.
'''

import random

class InvalidRank(Exception):
    pass

class InvalidSuit(Exception):
    pass

all_ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
all_suits = ['S', 'H', 'D', 'C']


class Card:
    '''
    Instances of this class represent a single card in a deck of 52.
    '''

    def __init__(self, rank, suit):
        '''
        Create a card given a valid rank and suit.
        
        Arguments:
          rank: the card rank (an integer between 2 and 10, or 'A', 'J', 'Q',
                or 'K')
          suit: either 'S' (spades), 'H' (hearts), 'D' (diamonds), 'C' (clubs)
        '''
        
        self.rank  = rank
        self.suit  = suit
        self.color = ''
        
        if rank not in all_ranks:
            # checking if card rank is valid
            raise InvalidRank(f'Invalid rank input to constructor: {rank}')
        
        if suit not in all_suits: 
            # checking if suit is valid
            raise InvalidSuit(f'Invalid suit input to constructor: {suit}')
        
        if suit == 'D' or suit == 'H': 
            # assigning color red to heart and diamond suits  
            self.color += 'red'
            
        elif suit == 'C' or suit == 'S':
            # assigning color red to heart and diamond suits            
            self.color += 'black'            


    def __str__(self):
        '''
        Return the string representation of the card.
        '''

        return f'{self.rank}{self.suit.lower()}'

    def goes_above(self, card):
        '''
        Return True if this card can go above 'card' on the foundations.

        Arguments:
          card -- another Card object

        Return value:
          True if this card can go above 'card' on the foundations i.e.
          if it has the same suit as 'card' and is one rank higher,
          otherwise False
        '''

        self.card = card
        
        # assert card input is a Card object
        assert isinstance(card, Card) 
        
        c = card  
        c_other = Card(self.rank, self.suit)
        if c.suit == c_other.suit:
            pos1 = all_ranks.index(c.rank) 
            pos2 = all_ranks.index(c_other.rank)
            if pos1 + 1 == pos2: 
                # check if rank of first card is one less than second card
                return True 
        else:
            return False

    def goes_below(self, card):
        '''
        Return True if this card can go below 'card' on a cascade.

        Arguments:
          card -- another Card object

        Return value:
          True if this card can go below 'card' on a cascade i.e.
          if it has the opposite color than 'card' and is one rank lower,
          otherwise False
        '''

        self.card = card
        assert isinstance(card, Card)
        
        c = card  
        c_other = Card(self.rank, self.suit)
        
        if c.color != c_other.color:
            # position of ranks of cards in all_ranks list
            pos1 = all_ranks.index(c.rank) 
            pos2 = all_ranks.index(c_other.rank)
            if pos1 - 1 == pos2:
                # check if rank of first card is one less than second card
                return True 
        else:
            return False


class Deck:
    '''
    Instances of this class represent a deck of 52 cards, 13 in each
    of four suits (spades (S), hearts (H), diamonds (D), and clubs (C).
    Ranks are 'A', 2 .. 10, 'J', 'Q', 'K'.
    '''
   
    def __init__(self):
        '''
        Initialize the Deck object.
        '''

        self.current = 0
        self.cards = []
        for x in all_ranks:
            for y in all_suits:
                # create every possible card combo
                self.cards += [Card(x, y)] 
                # shuffle cards
                shuffledDeck = random.shuffle(self.cards) 
                

    def __iter__(self):
        return self

    def __next__(self):
        '''
        Return the next card in the Deck, if there is one.
        '''
        
        deck = self.cards
        if self.current == 0:
            self.current = deck
        if len(self.current) == 0:
            raise StopIteration
        # return first Card object in list and then remove from the list'
        return self.current.pop(0) 
     