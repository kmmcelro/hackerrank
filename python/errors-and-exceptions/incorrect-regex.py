# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Incorrect Regex
# link: https://www.hackerrank.com/challenges/incorrect-regex/problem

""""
Task
You are given a string S.
Your task is to find out whether S is a valid regex or not.

This solution is for python 3, remove the if/else statement, keeping the try and except for python 2

import re

T = int(input())
for _ in range(T):
    s = raw_input()
    try:
        re.compile(s)
        print("True")
    except re.error:
        print("False")
"""


import re

T = int(input())
for _ in range(T):
    s = input()
    # Because in python 3 these are no longer invalid regex, this condition is needed for the outdated test cases
    if '*+' in s or '+?' in s or '++' in s:
        print('False')
    else:
        try:
            re.compile(s)
            print("True")
        except re.error:
            print("False")