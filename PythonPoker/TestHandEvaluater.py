'''
    Filename: TestHandEvaluater.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved

    This class is responsible for testing the 10 basic hands:
    0. High Card
    1. Pair
    2. 2 Pair
    3. Three of a Kind
    4. Straight
    5. Flush
    6. Full House
    7. Four of a Kind
    8. Straight Flush
    9. Royal Straight Flush (Ace high straight flush)
    
    Hand cards are selected to test the upper and lower bounds of the histogram
    list, and are inserted in the opposite of the desired order to test proper
    arrangement for the scoring function.
'''

import sys
from HandForge import *
import HandEvaluater


class TestHandEvaluater(object):

    def __init__(self):
        pass
    
    def test(self):
        print ("Test Commencing...")

        result = 0
        test_input = ""

        hand_eval = HandEvaluater.HandEvaluater()

        ''' ROYAL STRAIGHT FLUSH '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("10S JS QS KS AS"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)

        ''' STRAIGHT FLUSH '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("7D 8D 9D 10D JD"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)
        
        ''' FOUR OF A KIND '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("AC AH AD AC 2S"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)

        ''' FULL HOUSE / BOAT '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("2D 2C AS AC AD"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)
        
        ''' FLUSH '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("3S 10S 5S 8S AS"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)

        ''' STRAIGHT '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("AS QH KD JC 10H"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)
        
        ''' THREE OF A KIND '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("4C QD AC AH AS"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)

        ''' TWO PAIR '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("2S 5H 5C AH AH"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)
        
        ''' ONE PAIR '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("JS 10D 4H AD AC"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)

        ''' HIGH CARD '''
        scorecard = hand_eval.evaluate_hand(HandForge.create_single_hand("2S 10D 4H 8D AC"))
        print (str(scorecard.get_hand()) + " -  RESULT: HAND IS A " + scorecard.get_hand_type() + "  -  SCORE: " + scorecard.get_score() + os.linesep)


        print "Test Concluded."

tester = TestHandEvaluater()
tester.test()



''' Copyright 2017 - NorthBridge - All Rights Reserved '''