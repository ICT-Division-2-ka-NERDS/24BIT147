# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 12:17:13 2025

@author: Anouska
"""

from datetime import date

# Input two dates directly
d1_day, d1_month, d1_year = map(int, input("Enter first date (dd mm yyyy): ").split())
d2_day, d2_month, d2_year = map(int, input("Enter second date (dd mm yyyy): ").split())

# Create date objects
date1 = date(d1_year, d1_month, d1_day)
date2 = date(d2_year, d2_month, d2_day)

# Calculate absolute difference in days
difference = abs((date2 - date1).days)

# Output
print(f"Number of days between {date1} and {date2} is {difference} days.")

