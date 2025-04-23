# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:47:05 2025

@author: Anouska
"""

def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

s = input("Enter a string: ")
print("Lowercase:", to_lowercase(s))
print("Uppercase:", to_uppercase(s))
print("Toggle case:", toggle_case(s))
