'''
    Filename: Card.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved

    This class is responsible for encapsulating the card
    rank as an integer and a pointer to one of the class
    attributes of Suit (club, diamond, heart, spade).
'''

from Suit import *
import re


class Card(object):

    def __init__ (self, cardCode):
        regex = re.compile("([2-9])[cdhsCDHS]")
        if (regex.match(cardCode) != None):
            self._rank = int(cardCode[0])
            if cardCode[1].upper() == 'C':
                self._suit = Suit.CLUB
            elif cardCode[1].upper() == 'D':
                self._suit = Suit.DIAMOND
            elif cardCode[1].upper() == 'H':
                self._suit = Suit.HEART
            elif cardCode[1].upper() == 'S':
                self._suit = Suit.SPADE
            else:
                print "ERROR: Card Error 1"
                raise SystemExit
        else:
            regex = re.compile("[10]\d[cdhsCDHS]")
            if (regex.match(cardCode) != None):
                self._rank = int(cardCode[0:2])
                if cardCode[2].upper() == 'C':
                    self._suit = Suit.CLUB
                elif cardCode[2].upper() == 'D':
                    self._suit = Suit.DIAMOND
                elif cardCode[2].upper() == 'H':
                    self._suit = Suit.HEART
                elif cardCode[2].upper() == 'S':
                    self._suit = Suit.SPADE
                else:
                    print "ERROR: Card Error 2"
                    raise SystemExit
            else:
                
                regex = re.compile("[jqkaJQKA][cdhsCDHS]")
                if(regex.match(cardCode) != None):
                    if (cardCode[0].upper() == 'A'):
                        self._rank = 14
                    elif (cardCode[0].upper() == 'K'):
                        self._rank = 13
                    elif (cardCode[0].upper() == 'Q'):
                        self._rank = 12
                    elif (cardCode[0].upper() == 'J'):
                        self._rank = 11
                    else:
                        print "ERROR: Card Creation 3"
                        raise SystemExit
                    
                    if cardCode[1].upper() == 'C':
                        self._suit = Suit.CLUB
                    elif cardCode[1].upper() == 'D':
                        self._suit = Suit.DIAMOND
                    elif cardCode[1].upper() == 'H':
                        self._suit = Suit.HEART
                    elif cardCode[1].upper() == 'S':
                        self._suit = Suit.SPADE
                    else:
                        print "ERROR: Card Error 4"
                        raise SystemExit

    def compare_to(self, c):
        if self._rank == c._rank:
            if self._suit.compare_to(c._suit) < 0:
                return -1
            elif self._suit.compare_to(c._suit) > 0:
                return 1
            else:
                return 0
        elif self._rank < c._rank:
            return -1
        elif self._rank > c._rank:
            return 1
        else:
            print "Comparison Error"
            raise SystemExit


    def __str__(self):
        if self._suit is Suit.CLUB:
            suit_char = 'C'
        elif self._suit is Suit.DIAMOND:
            suit_char = 'D'
        elif self._suit is Suit.HEART:
            suit_char = 'H'
        elif self._suit is Suit.SPADE:
            suit_char = 'S'
        
        if(self._rank > 10):
            if (self._rank == 11):
                rank_char = 'J'
            elif (self._rank == 12):
                rank_char = 'Q'
            elif (self._rank == 13):
                rank_char = 'K'
            elif (self._rank == 14):
                rank_char = 'A'
            else:
                rank_char = 'E'
        else:
            rank_char = str(self._rank)
        return (rank_char + suit_char)

    def __lt__(self, other):
        if self._rank == other._rank:
            return self._suit < other._suit
        return self._rank < other._rank
    
    def __gt__(self, other):
        if self._rank == other._rank:
            return self._suit > other._suit
        return self._rank > other._rank
    
    def __eq__(self, other):
        if self._rank == other:
            return self._suit == other._suit
        return self._rank == other

    def get_suit(self):
        return self._suit


    def get_suit_rank(self):
        return self._suit


    def get_rank(self):
        return self._rank



''' Copyright 2017 - NorthBridge - All Rights Reserved '''