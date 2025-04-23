# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:24:16 2025

@author: Anouska
"""

def is_valid_triangle(a, b, c):
    if a + b + c == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

# Example
is_valid_triangle(60, 60, 60)
