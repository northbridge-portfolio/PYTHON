'''
    Filename: ScoreCard.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved

    This class is responsible for encapsulating:
        -The 64-bit numerical score as a string (for x86 systems)
        -The hand type as a string
        -The hand cards as a string
    
    Note that the 64-bitscore is designed to be compared against other
    hands. First, the hand type is assigned a value between 0 and 9.
    Second, the most valuable cards in the hand are sorted in descending 
    order, followed by the non-hand related cards. Third, the cards are
    assigned numerical values (2 = 02, J = 11, A = 14) and appended to 
    the overall hand ranking value. A sample score for the hand:
        2h 3h 4h 5h 6h = 90203040506 = Straight Flush
        2c 2d 2h 2s 3h = 70202020203 = Four of a Kind
'''


class ScoreCard(object):
    
    def __init__(self, score = None, handType = None, hand = None):
        self._score = score if score is not None else "0"
        self._hand_type = handType if handType is not None else ""
        self._hand = hand if hand is not None else ""

    def get_score(self):
        return self._score

    def get_hand_type(self):
        return self._hand_type

    def get_hand(self):
        return self._hand



''' Copyright 2017 - NorthBridge - All Rights Reserved '''