# Author: kmmcelro
# This is my solution to the Hackerrank challenge, String Split and Join
# link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

""""
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""


def split_and_join(line):
    line = line.split(" ") # turns the string into list of strings (with the words)
    line = "-".join(line) # combines back into one string using dashes inbetween words
    return line
    
if __name__ == '__main__': 
    line = input()
    result = split_and_join(line)
    print(result)