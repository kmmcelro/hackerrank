# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Capitalize!
# link: https://www.hackerrank.com/challenges/capitalize/problem

""""
Task
Given a full name, your task is to capitalize the name appropriately.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s2 = s[0].capitalize()
    for i in range(1,len(s)):
        if s[i-1] == ' ':
            s2 += s[i].capitalize()
        else:
            s2 += s[i]
    return s2
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
