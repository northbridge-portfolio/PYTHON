'''
    Filename: PermutationEngine.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved
    
    PermutationEngine.py is responsible for taking an input string,
    and generating all possible combinations of substitutions given
    a substitution list. To modify the default substitutions, please
    modify the configuration.ini file according to the instructions 
    included in the header of configuration.ini
'''

import sys
import copy
import itertools

class PermutationEngine(object):

    class Value_Subs:
        def __init__(self, value, subs):
            self.value, self.subs = value, subs


    def __init__(self, temp_dict):
        list_values = list(temp_dict["default_values"])
        list_subs = list(temp_dict["default_permutations"])
        i = 0
        while i < (len(list_values)):
            if (list_values[i].isspace() 
                or list_values[i] == "," 
                or list_values[i] == "(" 
                or list_values[i] == ")"):
                    list_values.remove(list_values[i])
                    list_subs.remove(list_subs[i])
                    continue
            i += 1
        self.default_values = list_values
        self.default_permutations = list_subs
        self.ppw = int(temp_dict["permutations_per_word"])
        self.pt = int(temp_dict["permutations_total"])
        if (str(temp_dict["include_original"]).lower()) == "false":
            self.include_original = False
        else:
            self.include_original = True


    def permutate(self, input_string):
        #A CREATE INDEX LIST
        input_string = list(input_string.rstrip('\n'))
        index_list_subs = []
        t_index_list_subs = []
        for i in range(len(input_string)):
            for j in range(len(self.default_values)):
                if input_string[i] is self.default_values[j]:
                    t_index_list_subs.append(i)
                    t_index_list_subs.append(self.default_permutations[j])
                    t_index_list_subs = tuple(t_index_list_subs)
                    index_list_subs.append(t_index_list_subs)
                    t_index_list_subs = []
        index_list_subs = tuple(index_list_subs)
        #A INDEXING OF REPLACEABLE CHARACTERS COMPLETED
        
        #B CREATE PERMUTATIONS
        # Determine if original string will be included with the output permutations
        # First combination (index 0) is always zero substitutions
        start = 0 if self.include_original else 1
        # (+1) is to account for original string if selected
        limit_ppw = self.ppw + 1 if self.include_original else self.ppw
        limit_pt = self.pt + 1 if self.include_original else self.pt
        
        return_string_list = []
        index_combinations = []
        perms_current = 0
        for i in range(start, limit_ppw):
            index_combinations = tuple(c for i in range(limit_ppw)
                                         for c in itertools.combinations(index_list_subs, i))
            perms_current += 1
        index_combinations = tuple(index_combinations)
        #B PERMUTATION CREATION COMPLETED        

        #C BEGIN REPLACEMENT OF INPUT STRING INDICES BASED ON INDEX-SUBSTITUTION LIST
        return_string = []
        perms_current = 0
        for i in range(start, len(index_combinations)):
            if (perms_current == limit_ppw) or (perms_current == limit_pt):
                return return_string_list
            return_string = copy.deepcopy(input_string)
            for j in range(len(index_combinations[i])):
                return_string[index_combinations[i][j][0]] = index_combinations[i][j][1]
            return_string_list.append("".join(return_string)+'\n')
            perms_current += 1
        return return_string_list
        #C REPLACEMENT OF INPUT STRING INDICES COMPLETED
   


''' Copyright 2017 - NorthBridge - All Rights Reserved '''