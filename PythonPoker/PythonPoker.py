'''
    Filename: PythonPoker.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved

    This is the main driver for the PythonPoker game.
    Run this module with no arguments and follow the command-line prompts.
'''

import re
#import TestHandEvaluater
import ScoreCard
import HandEvaluater
from HandForge import *


def run_game_five_card_draw(cards):
    hand = HandForge.create_single_hand(cards)
    hand_eval = HandEvaluater.HandEvaluater()
    return hand_eval.evaluate_hand(hand)

def run_game_texas_hold_em(cards):
    hand_eval = HandEvaluater.HandEvaluater()
    hand_permutations = HandForge.create_hand_permutations(cards)
    best_score = ScoreCard.ScoreCard()
    for element in hand_permutations:
        result = hand_eval.evaluate_hand(element)
        if int(result.get_score()) > int(best_score.get_score()):
            best_score = ScoreCard.ScoreCard(result.get_score(), result.get_hand_type(), result.get_hand())
    return best_score

#tester = TestHandEvaluater.TestHandEvaluater()
#tester.test()

def main():
    print "Game Commencing..."
    score_card = ScoreCard.ScoreCard("", "", "")
    user_option = "-1"
    while (user_option == "-1") or (user_option != "1") and (user_option != "2"):
        print ("Please select an option:" + os.linesep +
                       "1. 5 Card Draw" + os.linesep +
                       "2. Texas Hold 'Em" + os.linesep + 
                       "Enter Number: ")
        user_option = raw_input()
    
        if (user_option == "1"):
            while (True):
                print 'Please enter 5 cards (Example: "2c 3d 4h 5s 6c" or "10c jd qh ks ac" with no quotes)'
                input_cards = raw_input()
                # regex does not like multi-line triple-quoted strings - leave as-is
                regex = re.compile("((([2-9]|[10]\d|[jqkaJQKA])[cdhsCDHS])\s{1,}?){4}?(([2-9]|[10]\d|[jqkaJQKA])[cdhsCDHS]){1}?") 
                regex_result = regex.match(input_cards)
                if (regex_result):
                    #Check For Duplicate Cards
                    duplicate_flag = False
                    card_array = input_cards.split()
                    for card_one in range(len(card_array) - 1):
                        for card_two in range(card_one + 1, len(card_array)):
                            if card_array[card_one].upper() == card_array[card_two].upper():
                                print "Error: Duplicate Cards. Please check the format and try again."
                                duplicate_flag = True
                                break
                        if duplicate_flag:
                            break
                    if not duplicate_flag:
                        score_card = run_game_five_card_draw(regex_result.group())
                        break
                
        elif (user_option == "2"):
            while True:
                print 'Please enter 7 cards (Example: "2C 3D 4H 5S 6C 7D 8H" or "8C 9D 10H JS QC KD AH" with no quotes)'
                input_cards = raw_input()
                # regex does not like multi-line triple-quoted strings - leave as-is
                regex = re.compile("((([2-9]|[10]\d|[jqkaJQKA])[cdhsCDHS])\s{1,}?){6}?(([2-9]|[10]\d|[jqkaJQKA])[cdhsCDHS]){1}?")
                regex_result = regex.match(input_cards)
                if (regex_result):
                    #Check For Duplicate Cards
                    duplicate_flag = False
                    card_array = input_cards.split()
                    for card_one in range(len(card_array) - 1):
                        for card_two in range(card_one + 1, len(card_array)):
                            if card_array[card_one].upper() == card_array[card_two].upper():
                                print "Error: Duplicate Cards. Please check the format and try again."
                                duplicate_flag = True
                                break
                        if duplicate_flag:
                            break
                    if not duplicate_flag:
                        score_card = run_game_texas_hold_em(regex_result.group())
                        break
        else:
            pass
    
    
    if (score_card != None):
        print ("YOUR HAND: " + str(score_card.get_hand()) + " -  RESULT: HAND IS A " + 
               score_card.get_hand_type() + "  -  SCORE: " + score_card.get_score() + 
               os.linesep + os.linesep)
    else:
        print "There Is an Error With your input. Please Try again Using the correct format."


main()




''' Copyright 2017 - NorthBridge - All Rights Reserved '''