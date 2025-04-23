# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:16:12 2025

@author: Anouska
"""

def largest_smallest_two(a, b):
    if a > b:
        print("Largest:", a, "Smallest:", b)
    elif a < b:
        print("Largest:", b, "Smallest:", a)
    else:
        print("Both numbers are equal.")
largest_smallest_two(10, 20)
