# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Python If-Else
# link: https://www.hackerrank.com/challenges/py-if-else/problem

"""
Task: 
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird 
"""


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if 6 <= n <= 20: # All int values in [6, 20] range are considered weird
        print("Weird")
    elif n % 2 == 0: # All even numbers outside the range are not weird
        print("Not Weird")
    else: # Odd values outside the range are weird
        print("Weird")