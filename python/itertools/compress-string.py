# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Compress the String!
# link: https://www.hackerrank.com/challenges/compress-the-string/problem

""""
Task
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools.
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.
"""

from itertools import groupby

string = input()
groups = ""
for k,  g in groupby(string):
    group = list(g)
    repeatNum = len(group)
    groups += "("+ str(repeatNum)+ ", " + group[0] + ") "
    
print(groups)