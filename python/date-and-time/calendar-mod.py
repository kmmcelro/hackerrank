# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Calendar Module
# link: https://www.hackerrank.com/challenges/calendar-module/problem

""""
Task
You are given a date. Your task is to find what the day is on that date.
"""

from calendar import weekday 

Month, Day, Year = map(int, input().rstrip().split())

DofW = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

DofWIndice = weekday(Year,Month,Day)
print(DofW[DofWIndice])