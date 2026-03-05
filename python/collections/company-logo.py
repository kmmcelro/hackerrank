# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Company Logo
# link: https://www.hackerrank.com/challenges/most-commons/problem

""""
Task
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition. 
Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

* Print the three most common characters along with their occurrence count.
* Sort in descending order of occurrence count.
* If the occurrence count is the same, sort the characters in alphabetical order.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

dict = {}
for c in s: # stores each letter in the string into the dictionary along with the count
    dict[c] = s.count(c)
    
sortedDict = sorted(dict.items(), key=lambda item: (-item[1],item[0])) # sorting by value desc and then by letter
i = 0
for key in sortedDict:
    print(str(key[0]) + " "+ str(key[1]))
    i += 1
    if i == 3: # stop once top three are printed
        break
