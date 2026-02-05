# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Merge the Tools!
# link: https://www.hackerrank.com/challenges/merge-the-tools/problem

""""
Task
Consider the following:

A string, s, of length n where s = c0c1.....cn-1.
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. 
In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line  denotes string ui.
"""

def merge_the_tools(string, k):
    i = 1
    substring = ""
    for char in string:
        # Checking for distinctness of char in the current substring
        if char not in substring:
            substring += char   
        # cycling through k size chunks of the string
        if i == k: 
            i = 1
            print(substring)
            substring = ""
        else:
            i += 1

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)