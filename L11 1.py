# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:39:08 2025

@author: Anouska
"""

def get_valid_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            print("You entered:", num)
            break
        except ValueError:
            print("That's not a valid integer. Please try again.")
get_valid_integer()
