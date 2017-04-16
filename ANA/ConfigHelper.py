'''
    Filename: ConfigHelper.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved
    
    The ConfigHelper module is used to parse the Configuration.ini file
    located in the program directory, and extract the environment variables, 
    including permutations per word, permutations_total, etc.
    
    Please see the configuraiton.ini file for more information and usage.
'''

import ConfigParser


def generate_configuration_file(self):
        config_file = file("Configuration Write Test.ini", "wt")
        help_text = "# ANA CONFIGURATION FILE\n\n"\
        "# Default Values: Character values to be searched for and replaced\n\n"\
        "# Default Permutations To Be Replaced: the character to be replaced corresponds to the same index in\n"\
        "# 'Default Values' - ex. to change 'E', index #5 (0-based), replace '3' index #5 of 'Default Permutations'\n"\
        "# to the subsitution value desired\n\n"\
        "# Number of Permutations Per Word To Be Replaced: ex. 'academics', if value of permutations per word is\n"\
        "# set to 3, only the first three substitution letters ('a', 'a', 'e') will be replaced in the combinations\n"\
        "# generated.\n\n"\
        "# Default Number of Permutations Total Per Word: ex. 'academics' will use the number of permutations per\n"\
        "# word value to be begin generating permutations until the value specified by 'number of permutations\n"\
        "# total per word' is reached.  If there are less combinations for the words in the wordlist based on the\n"\
        "# other settings, then this limit will not be reached and can be ignored.\n\n"\
        "# Default Value of Progress Bar:  If set to True, the progress bar will be displayed during processing. Any\n"\
        "# other value will be considered false and the progress bar will not be displayed.\n\n"\
        "# Default Export Name: name of the new file to be written\n\n\n"\
        "# Subsitution Reference (Default Settings):\n"\
        "# ('a', 'A', 'b', 'B', 'e', 'E', 'g', 'G', 'i', 'I', 'l', 'L', 'o', 'O', 's', 'S')\n"\
        "# ('4', '4', '8', '8', '3', '3', '6', '6', '1', '1', '1', '1', '0', '0', '5', '5')\n\n\n"\
        "# ----------------------------------------------------------------------------------------------------\n\n"\
        "[SETTINGS]\n"\
        "# Default Values (CHARACTER/INTEGER)\n"\
        "default_values:       ('a', 'A', 'b', 'B', 'e', 'E', 'g', 'G', 'i', 'I', 'l', 'L', 'o', 'O', 's', 'S')\n"\
        "# Default Permutations (CHARACTER/INTEGER)\n"\
        "default_permutations: ('4', '4', '8', '8', '3', '3', '6', '6', '1', '1', '1', '1', '0', '0', '5', '5')\n"\
        "# Default Number Of Permutations Per Word (INTEGER)\n"\
        "permutations_per_word: 100\n"\
        "# Default Number of Permutations Total (INTEGER)\n"\
        "permutations_total: 100\n"\
        "# Default Value of Progress Bar (True/False)\n"\
        "progress_bar: True\n"\
        "# Default Value For \"Include Original?\"\n"\
        "include_original: True\n"\
        "# Default Export File Name Appendage (STRING)\n"\
        "append_name: [AUGMENTED]\n\n"\
        "# ----------------------------------------------------------------------------------------------------\n"
        config_file.write(help_text)
        config_file.close()

def parse_configuration():
        arg_dict = {}
        cf = ConfigParser.ConfigParser()
        try:
            cf.read("Configuration.ini")
        except:
            generate_configuration_file
            cf.read("Configuration.ini")
        cf_options = cf.items("SETTINGS")        
        # Copy over default settings from configuration.ini
        for item in cf_options:
            arg_dict[item[0]] = item[1]
        return arg_dict



''' Copyright 2017 - NorthBridge - All Rights Reserved '''