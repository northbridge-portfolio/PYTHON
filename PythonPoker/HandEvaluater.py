'''
    Filename: HandEvaluater.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved

    This class is responsible for evaluating individual hands.
    It evaluates them in descending order of value and returns 
    the first (highest) one found. 
'''

import ScoreCard


class HandEvaluater:

    rank_histogram = []
    suit_histogram = []

    def __init__(self):
        pass

    def evaluate_hand(self, hand):
        HandEvaluater.rank_histogram = hand.get_rank_histogram()
        HandEvaluater.suit_histogram = hand.get_suit_histogram()
        hand.sort()

        result = self.is_royal_straight_flush(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "ROYAL STRAIGHT FLUSH", str(hand))

        result = self.is_straight_flush(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "STRAIGHT FLUSH", str(hand))

        result = self.is_four_of_kind(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "FOUR OF A KIND", str(hand))

        result = self.is_full_house(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "FULL HOUSE", str(hand))

        result = self.is_flush(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "FLUSH", str(hand))

        result = self.is_straight(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "STRAIGHT", str(hand))

        result = self.is_three_of_kind(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "THREE OF A KIND", str(hand))

        result = self.is_two_pair(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "TWO PAIR", str(hand))

        result = self.is_pair(hand)
        if (int(result) > 0):
            return ScoreCard.ScoreCard(result, "PAIR", str(hand))

        result = self.rank_by_high_card(hand)
        return ScoreCard.ScoreCard(result, "HIGH CARD", str(hand))


    def calc_score(self, card_list, hand_rank):
        score_sum = hand_rank * 10000000000
        i = 0
        for element in card_list:
            if(i == 0):
                score_sum += card_list[i].get_rank() * 100000000
            elif(i == 1):
                score_sum += card_list[i].get_rank() * 1000000
            elif(i == 2):
                score_sum += card_list[i].get_rank() * 10000
            elif(i == 3):
                score_sum += card_list[i].get_rank() * 100
            else:
                score_sum += card_list[i].get_rank() * 1
            i += 1
        return str(score_sum)


    def is_royal_straight_flush(self, hand):
        if(int(self.is_straight_flush(hand)) > 0):
            if(HandEvaluater.rank_histogram[len(HandEvaluater.rank_histogram) - 1] > 0):
                hand.sort_reverse()
                return self.calc_score(hand.get_cards(), 9)
        return "0"

    def is_straight_flush(self, hand):
        if((int(self.is_straight(hand)) > 0) and (int(self.is_flush(hand)) > 0)):
            hand.sort_reverse()
            return self.calc_score(hand.get_cards(), 8)
        return "0"

    def is_four_of_kind(self, hand):
        for i in range(0, len(HandEvaluater.rank_histogram)):
            if(HandEvaluater.rank_histogram[i] == 4):
                return_list = []
                card_list = hand.get_cards()
                for j in range(len(card_list) - 1, -1, -1):
                    if (card_list[j].get_rank() == i + 2):
                        return_list.append(card_list[j])
                        del card_list[j]
                return_list = return_list + card_list
                return self.calc_score(return_list, 7)
        return "0"

    def is_full_house(self, hand):
        pair_flag = False
        triple_flag = False
        return_list = []
        card_list = hand.get_cards()
        for i in range(0, len(HandEvaluater.rank_histogram)):
            if(HandEvaluater.rank_histogram[i] == 2):
                if(triple_flag == False):
                    for j in range(len(card_list) - 1, -1, -1):
                        if(card_list[j].get_rank() == i + 2):
                            return_list.append(card_list[j])
                            del card_list[j]
                    pair_flag = True
                else:
                    return_list = return_list + card_list
                    hand.sort_reverse()
                    return self.calc_score(return_list, 6)

            if(HandEvaluater.rank_histogram[i] == 3):
                if(pair_flag == False):
                    for j in range(len(card_list) - 1, -1, -1):
                        if(card_list[j].get_rank() == i + 2):
                            return_list.append(card_list[j])
                            del card_list[j]
                    triple_flag = True
                else:
                    return_list = card_list + return_list
                    hand.sort_reverse()
                    return self.calc_score(return_list, 6)
        return "0"

    def is_flush(self, hand):
        for element in HandEvaluater.suit_histogram:
            if(element == 5):
                hand.sort_reverse()
                return self.calc_score(hand.get_cards(), 5)
        return "0"

    # Searches histogram backwards to return the highest possible straight first
    def is_straight(self, hand):
        for i in range(len(HandEvaluater.rank_histogram) - 1, 3, -1):
            if(((HandEvaluater.rank_histogram[i] == 1) and (HandEvaluater.rank_histogram[i - 1] == 1) and (HandEvaluater.rank_histogram[i - 2] == 1) \
               and (HandEvaluater.rank_histogram[i - 3] == 1) and (HandEvaluater.rank_histogram[i - 4] == 1))):
                hand.sort_reverse()
                return self.calc_score(hand.get_cards(), 4)
        return "0"

    def is_three_of_kind(self, hand):
        for i in range(0, len(HandEvaluater.rank_histogram)):
            if(HandEvaluater.rank_histogram[i] == 3):
                return_list = []
                card_list = hand.get_cards()
                for j in range(len(card_list) - 1, -1, -1):
                    if(card_list[j].get_rank() == i + 2):
                        return_list.append(card_list[j])
                        del card_list[j]
                return_list = return_list + card_list
                return self.calc_score(return_list, 3)
        return "0"

    def is_two_pair(self, hand):
        pair_flag = False
        return_list = []
        card_list = hand.get_cards()
        for i in range(0, len(HandEvaluater.rank_histogram)):
            if(HandEvaluater.rank_histogram[i] == 2):
                for j in range(len(card_list) - 1, -1, -1):
                    if(card_list[j].get_rank() == i + 2):
                        return_list.append(card_list[j])
                        del card_list[j]
                if(pair_flag == False):
                    pair_flag = True
                else:
                    return_list.sort()
                    return_list.reverse()
                    return_list = return_list + card_list
                    return self.calc_score(return_list, 2)
        return "0"

    def is_pair(self, hand):
        for i in range(0, len(HandEvaluater.rank_histogram)):
            if(HandEvaluater.rank_histogram[i] == 2):
                return_list = []
                card_list = hand.get_cards()
                for j in range(len(card_list) - 1, -1, -1):
                    if(card_list[j].get_rank() == i + 2):
                        return_list.append(card_list[j])
                        del card_list[j]
                card_list.sort(reverse=True)
                return_list = return_list + card_list
                return self.calc_score(return_list, 1)
        return "0"

    def rank_by_high_card(self, hand):
        hand.sort_reverse()
        return self.calc_score(hand.get_cards(), 0)



''' Copyright 2017 - NorthBridge - All Rights Reserved '''