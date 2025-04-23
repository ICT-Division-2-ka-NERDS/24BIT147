# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:04:09 2025

@author: Anouska
"""

def remove_substring(original, to_remove):
    i = 0
    while i <= len(original) - len(to_remove):
        match = True
        for j in range(len(to_remove)):
            if original[i + j] != to_remove[j]:
                match = False
                break
        if match:
            return original[:i] + original[i + len(to_remove):]
        i += 1
    return original  # return original if substring not found
original = input("Enter the original string: ")
to_remove = input("Enter the string to remove: ")
result = remove_substring(original, to_remove)
print("Final string after removal:", result)
