'''
    Filename: Suit.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved

    This class is responsible for encapsulating:
        -The hand type as a string
        -The 
'''


class Suit(object):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3
    
    def __init__ (self, ranking):
        self._suit = ranking

    def __lt__ (self, other):
        ''' Suit order value in ascending order CLUB < DIAMONDS < HEARTS < SPADES '''
        if(self._suit == other._suit):
            return 0
        else:
            return self._suit - other._suit

    def __str__ (self):
        returnChar = ''
        if(self._suit == 0):
            return_char = 'C'
        elif(self._suit == 1):
            return_char = 'D'
        elif(self._suit == 2):
            return_char = 'H'
        elif(self._suit == 3):
            return_char = 'S'
        return return_char

    def get_suit_rank(self):
        return self._suit



''' Copyright 2017 - NorthBridge - All Rights Reserved '''