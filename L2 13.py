# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:30:49 2025

@author: Anouska
"""

def number_to_word(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if 0 <= n <= 19:
        print(words[n])
    else:
        print("Out of range")
number_to_word(15)
