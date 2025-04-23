# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:30:10 2025

@author: Anouska
"""

import math

def point_circle_relation(cx, cy, radius, px, py):
    distance = math.sqrt((px - cx)**2 + (py - cy)**2)
    if distance < radius:
        print("Inside the circle")
    elif distance == radius:
        print("On the circle")
    else:
        print("Outside the circle")
point_circle_relation(0, 0, 5, 3, 4)
