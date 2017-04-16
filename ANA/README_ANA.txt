Program: ANA.p
Author: NorthBridge
Program Version 3.4
Python Version: 2.7
Copyright 2017 - NorthBridge - All Rights Reserved


## OVERVIEW:
   ANA (Alpha Numeric Augmenter) is a tool to modify existing word lists, 
   by substituting numbers for letters, as is common for people to do when 
   attempting to strengthen their password. This program can be duplicated 
   in John the Ripper using the appropriate parameters. However, this program 
   is designed to output a completely new file with the augmented results.


## USAGE:
   This program is interactively driven from the console. It will prompt you 
   for the file to be augmented, the number of permutations per word, the
   number of permutations total, and whether to include the original word 
   before augmentation.

   To view a sample, when prompted for a filename, simply enter "-sample"
   (with no quotes) and a sample file will be generated, augmented, and 
   checked for accuracy.


## ADDITIONAL NOTES:
   Please see the configuraiton.ini file for more information and usage.
   Note: Default values and substitutions can be changed permanently by 
   modifying the Configuration.ini file. These changes will be kept until 
   the Configuration.ini file is deleted (and a new one is created using 
   the default settings) or modified by the user back to the original values.
