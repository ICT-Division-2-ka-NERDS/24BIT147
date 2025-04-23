# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:24:47 2025

@author: Anouska
"""


employees = {
    101: [("E001", 50000), ("E002", 75000), ("E007", 47000)],
    102: [("E003", 62000), ("E004", 41000)],
    103: [("E005", 55000), ("E006", 92000)]
}

print("Department-wise Minimum and Maximum Salaries:\n")

for dept, records in employees.items():
   
    salaries = [salary for _, salary in records]
    min_salary = min(salaries)
    max_salary = max(salaries)

    print(f"Department {dept} → Min: {min_salary}, Max: {max_salary}")
