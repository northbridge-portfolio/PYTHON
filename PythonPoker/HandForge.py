'''
    Filename: HandForge.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved

    This class is responsible for creating both single hands
    as well as create hand permutations for the Texas Hold 'Em game.
'''

import os
import Hand

class HandForge(object):
    
    def __init__(self):
        pass

    @classmethod
    def create_single_hand(cls, hand_string):
        return Hand.Hand(hand_string.split(" "))

    @classmethod
    def create_hand_permutations(cls, hand_string):
        hand_permutations = []
        card_string_array = hand_string.split(" ")
        if(len(card_string_array) == 7):
            for i in range(0, len(card_string_array) - 2):
                for j in range(i + 1, len(card_string_array) - 1):
                    for k in range(j + 1, len(card_string_array) - 0):
                        for m in range(k + 1, len(card_string_array) - 0):
                            for n in range(m + 1, len(card_string_array) - 0):
                                hand_combination = [card_string_array[i], 
                                                    card_string_array[j], 
                                                    card_string_array[k], 
                                                    card_string_array[m], 
                                                    card_string_array[n]]
                                hand = Hand.Hand(hand_combination)
                                hand_permutations.append(hand)
        else:
            print "ERROR: Invalid card input, please try again. Program will now exit."
            raise SystemExit
        return tuple(hand_permutations)

    def __str__(self):
        return_string = ""
        for element in HandForge.hand_permutations:
            return_string += str(element) + os.linesep
        return return_string



''' Copyright 2017 - NorthBridge - All Rights Reserved '''