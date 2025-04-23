# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:29:10 2025

@author: Anouska
"""

def are_points_colinear(x1, y1, x2, y2, x3, y3):
    if (y2 - y1)*(x3 - x1) == (y3 - y1)*(x2 - x1):
        print("Points are colinear")
    else:
        print("Points are not colinear")
are_points_colinear(1, 2, 2, 4, 3, 6)
