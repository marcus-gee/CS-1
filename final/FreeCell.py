# Name: Marcus Gee
# CMS cluster login name: mcgee
#
# CS 1 Final exam, 2017
#

'''
This module has classes that implement a FreeCell game.
'''

import random
from Card import *

class IllegalMove(Exception):
    '''
    Exception class representing illegal moves in a FreeCell game.
    '''
    pass

class FreeCell:
    '''
    A FreeCell game is represented by the following data structures:
      -- the foundation: a dictionary mapping suits to ranks
         e.g. { 'S' : 'A', 'D': 2 }  # other two suits (H, C) empty
      -- the freecells: a list four cards (or None if no card)
      -- the "cascades": a list of eight lists of cards
    '''

    def __init__(self):
        self.foundation = {}   # suit -> number map 
        self.freecell   = [None] * 4
        self.cascade    = [None] * 8

        # Deal cards from a full deck to the cascades.
        i = 0   # current cascade #
        for card in Deck():
            if self.cascade[i] == None:
                self.cascade[i] = []
            self.cascade[i].append(card)
            i = (i + 1) % 8

    def game_is_won(self):
        '''
        Return True if the game is won.
        '''
        
        key_list = ['S', 'H', 'D', 'C']
        suit_list = ['K', 'K', 'K', 'K']
        win = False
        # for win to occur check that foundation dictionary keys are kings and 
        # freecells and cascades are empty
        for key in key_list:
            if self.foundation.get(key) == 'K':
                for x in range(4):
                    if self.freecell[x] == None:
                        for y in range(8):
                            if self.cascade[y] == []:
                                win = True
        return win
    #
    # Movement-related functions.
    #

    def move_cascade_to_freecell(self, n):
        '''
        Move the bottom card of cascade 'n' to the freecells.
        Raise an IllegalMove exception if the move can't be made.
        '''

        if n not in range(8) or type(n) != int: 
            raise IllegalMove('argument must be an integer from 0 to 7')
        if None not in self.freecell:
            raise IllegalMove('there are no empty freecells; card cannot '
            'be moved.')
        if self.cascade[n] == []:
            raise IllegalMove('cascade you are attempting to move from is '
            'empty')
        else:
            # card to move is the card in the bottom of the cascade
            card_to_move = self.cascade[n][-1]
            # remove the card from the cascade
            self.cascade[n].remove(card_to_move)
            for x, y in enumerate(self.freecell): # add card to empty freecell
                if y == None:
                    self.freecell[x] = card_to_move
                    return
            
        

    def move_freecell_to_cascade(self, m, n):
        '''
        Move freecell card 'm' to cascade 'n'.
        Raise an IllegalMove exception if the move can't be made.
        '''

        
        # illegal move errors
        if m not in range(4) or type(m) != int:
            raise IllegalMove('argument must be an integer from o to 3')
        if n not in range(8) or type(n) != int:
            raise IllegalMove('argument must be an integer from 0 to 7')
        if self.freecell[m] == None:
            raise IllegalMove('cannot move from an empty freecell')
        
        card_to_move = self.freecell[m] 
        
        # empty cascade
        if self.cascade[n] == []: 
            self.cascade[n].append(card_to_move)
            self.freecell[m] = None
            return
        
        if card_to_move.goes_below(self.cascade[n][-1]) == True: 
            self.cascade[n].append(card_to_move)
            self.freecell[m] = None    
            
        # raise error if card cannot go below
        else: 
            raise IllegalMove('invalid move; the card on the freecell must be '
                              'one lower in rank than the card at the end of '
                              'the cascade and of opposite color')        

    def move_cascade_to_cascade(self, m, n):
        '''
        Move a single card from one cascade to another.
        Raise an IllegalMove exception if the move can't be made.
        '''

        # illegal move errors
        if m not in range(8) or type(m) != int:
            raise IllegalMove('argument must be an integer from 0 to 7')
        if n not in range(8) or type(n) != int:
            raise IllegalMove('argument must be an integer from 0 to 7')
        if self.cascade[m] == []:
            raise IllegalMove('attempted to remove card from an empty cascade')  
        
        # card being moved from the cascade
        lowest_cascade_card = self.cascade[m][-1]
        
        if self.cascade[n] == []: # empty cascade
            self.cascade[n].append(lowest_cascade_card)
            self.cascade[m].remove(lowest_cascade_card)
            return
        
        # card above where we want to move the card
        card_above = self.cascade[n][-1]
        
        if lowest_cascade_card.goes_below(card_above) == True:
            self.cascade[n].append(lowest_cascade_card)
            self.cascade[m].remove(lowest_cascade_card)        
            return 
 
        else:
            raise IllegalMove('invalid move; the card moving from the cascade '
                              'must be one lower in rank than the card at the '
                              'end of the cascade and of opposite color')        
        
    def move_cascade_to_foundation(self, n):
        '''
        Move the bottom card of cascade 'n' to the foundation.
        If there is no card, or if the bottom card can't go to the foundation,
        raise an IllegalMove exception.
        '''

        # illegal move errors
        if n not in range(8) or type(n) != int:
            raise IllegalMove('argument must be an integer from 0 to 7')
        if self.cascade[n] == []:
            raise IllegalMove('attempted to remove card from an empty cascade')
                  
        # card being moved from the cascade
        lowest_cascade_card = self.cascade[n][-1] 
        suit                = lowest_cascade_card.suit.upper()
        rank                = lowest_cascade_card.rank
        
        if suit not in self.foundation:
            if rank == 'A':
                self.cascade[n].remove(lowest_cascade_card)                
                self.foundation[suit] = rank
            else:
                raise IllegalMove('invalid move; the foundation bottom card' 
                                  'must be ace')                
        else:
            foundation_top_card = Card(self.foundation[suit], suit)
        
            if lowest_cascade_card.goes_above(foundation_top_card) == True:
                self.cascade[n].remove(lowest_cascade_card)
                self.foundation[suit] = rank
                return  
            
            else:
                raise IllegalMove('invalid move; the card moving from the '
                                  'cascade must be one higher in rank than the '
                                  'card at the top of the foundation and of '
                                  'same suit')            
                
                
    def move_freecell_to_foundation(self, n):
        '''
        Move the card at index 'n' of the freecells to the foundation.
        If there is no card there, or if the card can't go to the foundation,
        raise an IllegalMove exception.
        '''

        
        # illegal move errors
        if n not in range(4) or type(n) != int:
            raise IllegalMove('argument must be an integer from 0 to 4')
        if self.freecell[n] == None:
            raise IllegalMove('attempted to remove from freecell with no card')
                  
        # card being moved from the cascade
        freecell_card = self.freecell[n] 
        suit          = freecell_card.suit.upper()
        rank          = freecell_card.rank
        
        if suit not in self.foundation:
            if rank == 'A':
                self.freecell[n] = None               
                self.foundation[suit] = rank
            else:
                raise IllegalMove('invalid move; the foundation bottom card' 
                                  'must be ace')                
        else:
            foundation_top_card = Card(self.foundation[suit], suit)
        
            if freecell_card.goes_above(foundation_top_card) == True:
                self.freecell[n] = None
                self.foundation[suit] = rank
                return  
            
            else:
                raise IllegalMove('invalid move; the card moving from the '
                                  'freecell must be one higher in rank than '
                                  'the card at the top of the foundation and '
                                  'of same suit')            
                

