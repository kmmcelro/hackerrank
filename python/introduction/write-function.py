# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Write a Function
# link: https://www.hackerrank.com/challenges/write-a-function/problem

""""
Task
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
"""

def is_leap(year):
    # Write your logic here

    if year % 400 == 0: # all years divisible by 100 and 4 are divisible by 400, so they're all leap years
        return True
    elif year % 100 == 0: # all years divisible by 100 that aren't by 400 aren't leap years
        return False
    if year % 4 == 0: # the rest of the years divisible by 4 are leap years
        return True
    else: # the rest are not leap years
        return False
    
year = int(input())
print(is_leap(year))