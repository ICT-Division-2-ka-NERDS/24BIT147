# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:43:09 2025

@author: Anouska
"""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)
user_input = input("Enter a string: ")
count_vowels(user_input)
