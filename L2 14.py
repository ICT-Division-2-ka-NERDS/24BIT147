# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 00:31:28 2025

@author: Anouska
"""

def subject_grade(mark):
    if mark == "Absent":
        return "NA"
    mark = int(mark)
    if mark <= 39:
        return "F"
    elif mark <= 44:
        return "P"
    elif mark <= 49:
        return "C"
    elif mark <= 54:
        return "B"
    elif mark <= 59:
        return "B+"
    elif mark <= 69:
        return "A"
    elif mark <= 79:
        return "A+"
    elif mark <= 100:
        return "O"
    else:
        return "Invalid"

def evaluate_student(m1, m2, m3):
    marks = [m1, m2, m3]
    total = 0
    fail = False
    for m in marks:
        if m != "Absent":
            m = int(m)
            total += m
            if m <= 39:
                fail = True
        else:
            fail = True
    average = total / 3
    print("Total:", total)
    print("Average:", average)
    for i, m in enumerate(marks):
        print(f"Subject {i+1} Grade:", subject_grade(m))
    print("Result:", "Fail" if fail else "Pass")

evaluate_student("45", "60", "Absent")
