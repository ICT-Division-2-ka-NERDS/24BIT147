# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:28:01 2025

@author: Anouska
"""

def rectangle_area_vs_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    if area > perimeter:
        print("Area is greater")
    else:
        print("Perimeter is greater or equal")
rectangle_area_vs_perimeter(5, 10)
