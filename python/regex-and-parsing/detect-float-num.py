# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Detect Floating Point Number
# link: https://www.hackerrank.com/challenges/introduction-to-regex/problem

""""
Task
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

* Number can start with +, - or . symbol.
* Number must contain at least 1 decimal value.
* Number must have exactly one . symbol.
* Number must not give any exceptions when converted using float(N).

"""


import re

floatpattern = re.compile(r'^[-+\.]?\d*\.\d*$') 

n = int(input())

for i in range(0,n):
    floatNum = input()
    floatflag = True
    try: 
        j = float(floatNum) 
    except ValueError:
        floatflag = False
    if floatpattern.match(floatNum) and floatflag:
        print("True")
    else:
        print("False")
