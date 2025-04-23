# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:32:48 2025

@author: Anouska
"""

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1.find(string2) != -1:
    print(f'"{string2}" is found in "{string1}"')
elif string2.find(string1) != -1:
    print(f'"{string1}" is found in "{string2}"')
else:
    print("Neither string is found in the other.")
