'''
    Filename: ana.py
    Author: NorthBridge
    Python Version: 2.7
    Copyright 2017 - NorthBridge - All Rights Reserved
    
    ANA (Alpha Numeric Augmenter) is a tool to modify existing word lists,
    by substituting numbers for letters, as is common for people to do when
    attempting to strengthen their password. This program can be duplicated
    in John the Ripper using the appropriate parameters. However, this program
    is designed to output a completely new file with the augmented results.
    
    Please see the configuraiton.ini file for more information and usage.
'''

import os
import sys
import ConfigParser
from ConfigHelper import *
import PermutationEngine


def augment(file_name, append_name, engine):
    new_file_name = "".join([file_name[:file_name.rfind(".")], 
                             "_", append_name, ".txt"])
    
    ''' Open Buffered Reader/Writer objects using default block sizes
        determined by isatty() system report - usually 4096 or 8192 '''
    output_file = file(new_file_name, "wt")
    
    with open(file_name) as original_file:
        for line in original_file:
            line_list = engine.permutate(line)
            for item in line_list:
                output_file.write(item)

def generate_sample_file():
    print "Generating sample..."
    try:
        input_file = file("ana_sample_input.txt", "wt")
        input_file.write("alpha\nnumeric\naugmenter\n")
    except:
        print "Error creating sample input file"
    finally:
        input_file.close()
    arg_dict = parse_configuration()
    if arg_dict is None:
        print """There is an error with the \"Configuration.ini\" file. 
                 It may be missing or corrupted."""
        return 1
    engine = PermutationEngine.PermutationEngine(arg_dict)
    augment("ana_sample_input.txt", "augmented", engine)
    print "Sample complete."
    return check_sample_file()

def check_sample_file():
    sample_file = open("ana_sample_input_augmented.txt", "r")
    line = sample_file.readline()
    sample_string = ""
    
    with open("ana_sample_input_augmented.txt", "r") as sample_file:
        for line in sample_file:
            sample_string += line
    
    #print sample_string
    sample_check = "alpha\n4lpha\na1pha\nalph4\n41pha\n4lph4\na1ph4\n41ph4\nnumeric\nnum3ric\nnumer1c\nnum3r1c\naugmenter\n4ugmenter\nau6menter\naugm3nter\naugment3r\n4u6menter\n4ugm3nter\n4ugment3r\nau6m3nter\nau6ment3r\naugm3nt3r\n4u6m3nter\n4u6ment3r\n4ugm3nt3r\nau6m3nt3r\n4u6m3nt3r\n"
    #print sample_check
    if sample_string == sample_check:    
        print "Sample file check successful."
        return 0
    else:
        print "Sample file check failed"
        return 1
 

def main():
    path_delimiter = "\\"    
    if len(sys.argv) > 1:
        if sys.argv[1] == "-sample":
            return generate_sample_file()

    filename = ""
    while not os.path.isfile(filename):
        print ("Enter the filename of the wordlist to be augmented (cwd = " + 
               os.getcwd().rpartition(os.path.sep)[2] + ") [enter -sample to produce a sample augmented file]: ")
        filename = raw_input()
        if filename.upper() == "-SAMPLE":
            return generate_sample_file()
        if os.path.isfile(filename):
            break
        else:
            print "Invalid filename. Please try again.\n"
        
    # Get Permutations Per Word (PPW)
    ppw = "-1"
    while (not (ppw.isdigit())) and ((ppw < 0) or (ppw > 100)):
        print "Please enter the permutations per word (ppw) [default max]: "
        ppw = raw_input()
        if ppw is not "":
            if ppw.isdigit():
                if ((int(ppw) > 0) and (int(ppw) < 101)):
                    break
                else:
                    ppw = ""
                    print "Invalid input. Please enter an integer (0-100).\n"
            else:
                print "Invalid input. Please enter an integer (0-100).\n"
        else:
            print "Using default value"
            break
        
    # Get Permutations Total (PT)
    pt = "-1"
    while (pt is not "") or ((not (pt.isdigit())) and ((pt < 0) or (pt > 100))):
        print "Please enter the permutations total (pt) [default max]: "
        pt = raw_input()
        if pt is not "":
            if pt.isdigit():
                if ((int(pt) > 0) and (int(pt) < 101)):
                    break
                else:
                    pt = ""
                    print "Invalid input. Please enter an integer (0-100).\n"
            else:
                print "Invalid input. Please enter an integer (0-100).\n"
        else:
            print "Using default value"
            break

    # Include Original - accept 'Y' or 'N'
    user_input = "-1"
    include_original = True
    while ((user_input.upper() != 'Y') and 
          (user_input.upper() != 'N') and
          (user_input != '')):
        print "Include original word? Enter 'Y'/'N' [default = 'Y']: "
        user_input = raw_input()
        if user_input != "":
            if user_input.upper() == 'Y':
                include_original = True
            elif user_input.upper() == 'N':
                include_original = False
            else:
                print ("Invalid input. Please enter either 'Y' or 'N' or (leave blank for default.)\n")
        else:
            print "Using default value"


    arg_dict = parse_configuration()
    if arg_dict is None:
        print ("""There is an error with the 'Configuration.ini' file. 
                It may be missing or corrupted.""")
    
    if ppw is not "":
        arg_dict['permutations_per_word'] = ppw
    if pt is not "":
        arg_dict['permutations_total'] = pt
    if include_original != "":
        arg_dict['include_original'] = include_original
    
    print "Test Commencing..."
    engine = PermutationEngine.PermutationEngine(arg_dict)
    augment(filename, arg_dict["append_name"], engine)
    print "Test Complete."
    return 0


main()



''' Copyright 2017 - NorthBridge - All Rights Reserved '''