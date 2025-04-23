# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:23:44 2025

@author: Anouska
"""

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
is_leap_year(2024)
