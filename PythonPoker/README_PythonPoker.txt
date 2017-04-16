Program: PythonPoker.py
Author: NorthBridge
Program Version 2.2
Python Version: 2.7
Copyright 2017 - NorthBridge - All Rights Reserved


## OVERVIEW:
   This program evaluates a group of cards (a poker hand) for nine of the most 
   common poker hands. These include in ascending order of value:
   0. High Card
   1. One Pair
   2. Two Pair
   3. Three of a Kind
   4. Straight
   5. Flush
   6. Full House
   7. Four of a Kind
   8. Straight Flush
   9. Royal Straight Flush (Ace High Straight Flush)

## USAGE:
   This program is to be run with no command line arguments. Please follow the 
   prompts at the console and follow the directions given. If the game 
   "Five Card Draw" is selected, five valid cards must be entered. If the game 
   "Texas Hold 'Em" is selected, seven valid cards must be entered.

   Card strings must be entered in the following format:
   "RS RS RS RS RS" or "RS RS RS RS RS RS RS" with no surrounding quotes.
   where: R is a Rank (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)
          S is a Suit (C, D, H, S) [C=Club, D=Diamond, H=Heart, S=Spade]
          *Suit is case insensitive
   Example 1: "2S 3S 4S 5S 6S" with no surrounding quotes
   Example 2: "10C JS QH KS AD" with no surrounding quotes


## ADDITIONAL NOTES:
   This program outputs a ScoreCard object, representing the result of the hand
   in the form of a 64-bit integer stored as a string for compatibility. This 
   ScoreCard contains a formatted score unique to each hand and can be compared 
   against another ScoreCard generated using the same algorithm.

   The ScoreCard value is computed using the following algorithm:
   First, the hand type is assigned a value between 0 and 9.
    Second, the most valuable cards in the hand are sorted in descending 
    order, followed by the non-hand related cards. Third, the cards are
    assigned numerical values (2 = 02, J = 11, A = 14) and appended to 
    the overall hand ranking value. A sample score for the hand:
        2h 3h 4h 5h 6h = 90203040506 = Straight Flush
        2c 2d 2h 2s 3h = 70202020203 = Four of a Kind