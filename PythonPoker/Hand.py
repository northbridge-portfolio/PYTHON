'''
    Filename: Hand.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved

    This class is responsible for encapsulating cards
    into a list of Cards called called_list. 
'''

from Suit import *
import Card


class Hand(object):

    # Constructor terminates on error. 
    # Could consider throwing an exception and passing this back to the caller 
    # for corrected user input.
    def __init__(self, hand_string_array):
        card_list = []
        for element in hand_string_array:
            card_list.append(Card.Card(element))
        self._hand = tuple(card_list)

    def get_rank_histogram(self):
        #temp_hist = []
        rank_count = [0] * 13
        for index in range(0, len(self._hand)):
            rank_count[self._hand[index].get_rank() - 2] += 1
        return rank_count

    def get_suit_histogram(self):
        suit_count = [0] * 4
        for element in self._hand:
            if element.get_suit() is Suit.CLUB:
                suit_count[element.get_suit_rank()] += 1
            elif element.get_suit() is Suit.DIAMOND:
                suit_count[element.get_suit_rank()] += 1
            elif element.get_suit() is Suit.HEART:
                suit_count[element.get_suit_rank()] += 1
            elif element.get_suit() is Suit.SPADE:
                suit_count[element.get_suit_rank()] += 1
        return suit_count


    def __str__(self):
        s = ""
        for element in self._hand:
            s += str(element) + " "
        return s


    def get_cards(self):
        return list(self._hand)

    def sort(self):
        temp_list = list(self._hand)
        temp_list.sort()
        if(temp_list is not None):
            self._hand = tuple(temp_list)
            return self._hand
        else:
            print "SORTING ERROR"
    
    def sort_reverse(self):
        temp_list = list(self._hand)
        temp_list.sort(reverse=True)
        if(temp_list is not None):
            self._hand = tuple(temp_list)
            return self._hand
        else:
            print "REVERSE SORTING ERROR"



''' Copyright 2017 - NorthBridge - All Rights Reserved '''