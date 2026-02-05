# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Text Wrap
# link: https://www.hackerrank.com/challenges/text-wrap/problem

""""
Task
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.
"""

import textwrap

def wrap(string, max_width):
    i = 1 # declare to track current width
    s = ""
    for char in string:
        s += char
        if i == max_width: #adds a new line
            s += "\n"
            i = 0 # back to zero because it's a new line
        i += 1 # increases to account for next number
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)