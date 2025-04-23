# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:17:52 2025

@author: Anouska
"""

def largest_smallest_three(a, b, c):
    largest = a
    smallest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    print("Largest:", largest, "Smallest:", smallest)
largest_smallest_three(3, 5, 1)
