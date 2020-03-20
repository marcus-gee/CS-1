# Name: Marcus Gee
# CMS cluster login name: mcgee
#
# CS 1 Final exam, 2017
#

'''
This module has functions and classes that augment the base FreeCell
object to produce a more full-featured FreeCell game.
'''

import random
from Card import *
from FreeCell import *

# Supplied to students:
def max_cards_to_move(nc, nf):
    '''
    Return the maximum number of cards that can be moved as a single sequence
    if the game has 'nc' empty cascades and 'nf' empty freecells.
    If the target cascade is empty then subtract 1 from 'nc'.

    Arguments:
      nc -- number of empty non-target cascades
      nf -- number of empty freecells

    Return value:
      the maximum number of cards that can be moved to the target
    '''

    assert type(nc) is int
    assert 0 <= nc <= 8
    assert type(nf) is int
    assert 0 <= nf <= 4

    return 1 + nf + sum(range(1, nc + 1))

def longest_movable_sequence(cards):
    '''
    Compute the length of the longest sequence of cards at the end of a 
    list of cards that can be moved in a single move.  Cards in the sequence 
    must be in strict descending order and alternate colors.

    Arguments:
      cards -- a list of cards

    Return value:
      the number of cards at the end of the list forming the longest
      sequence
    '''

    assert type(cards) is list
    for c in cards:
        assert isinstance(c, Card)
    
    count = 0
    prev_card = None
    for c in cards[::-1]:
        if count == 0:
            count += 1
            prev_card = c
        else:
            if prev_card.goes_below(c):
                count += 1
                prev_card = c
            else:
                return count 
    return count

def ok_to_automove(card, foundation):
    '''
    Return True if a card can be automoved to a foundation.

    Arguments:
      card       -- a Card object
      foundation -- a foundation dictionary (mapping suits to ranks)
    
    [C, S, H, D] ordered
    
    Return value:
      True if the card can be automoved, else False
    '''

    assert isinstance(card, Card)
    assert type(foundation) is dict
    
    suits = ['C', 'S', 'H', 'D']
    if card.rank == 'A':
        return True
    
    for s in suits:
        if card.suit == s:
            if card.suit in foundation:
                return card.goes_above(Card(foundation[card.suit], s))  
        else:
            if (s not in foundation) or (foundation[s] < (card.rank - 1)):
                return False
    
        
class FreeCellFull(FreeCell):
    '''
    FreeCellFull is an enhanced version of FreeCell with extra useful
    features.
    '''

    def multi_move_cascade_to_cascade(self, m, n, p):
        '''
        Move a sequence of 'p' cards from cascade 'm' to cascade 'n'.
        Cascade 'm' must have at least 'p' cards.  The last 'p'
        cards of cascade 'm' must be in descending rank order and
        alternating colors.

        If the move can't be made, raise an IllegalMove exception.

        Arguments:
          m, n -- cascade indices (integers between 0 and 7)
          p    -- an integer >= 0

        Return value: none
        '''
        # use longest_moveable_sequence(cascade[m]) to make sure its p
        # 
        
        # illegal move errors
        if m not in range(8) or type(m) != int:
            raise IllegalMove('argument must be an integer from 0 to 7')
        if n not in range(8) or type(n) != int:
            raise IllegalMove('argument must be an integer from 0 to 7')
        if p < 0 or type(p) != int:
            raise IllegalMove('argument must be an integer of at least 0')
        if len(self.cascade[m]) < p:
            raise IllegalMove('trying to move too many cards from cascade')  
        if p == 0:
            return
        
        seq_len = longest_movable_sequence(self.cascade[m])
        if seq_len >= p:
            cards_to_move = self.cascade[m][-p:]
            # just one card -> make into list for later
            #if type(cards_to_move) != list:
                #cards_to_move = [cards_to_move]
                
            if self.cascade[n] == []: # empty cascade
                for c in cards_to_move: 
                    self.cascade[n].append(c)
                    self.cascade[m].remove(c)
                return 
                
            # card above where we want to move the card
            card_above = self.cascade[n][-1]
            top_card      = cards_to_move[0]
            if top_card.goes_below(card_above) == True:
                for c in cards_to_move:
                    self.cascade[n].append(c)
                    self.cascade[m].remove(c)        
                return 
            else:
                raise IllegalMove('invalid move; the card moving from the cascade '
                                  'must be one lower in rank than the card at the '
                                  'end of the cascade and of opposite color') 
        else:
            raise IllegalMove('invalid move; no movable seq is long enough')         
                   

    def automove_to_foundation(self, verbose=True):
        '''
        Make as many moves as possible from the cascades/freecells to the
        foundations.

        Argument:
          verbose -- if True, print a message when each card is automoved

        Return value: none
        '''

        pass  # TODO

