# Author: kmmcelro
# This is my solution to the Hackerrank challenge, sWAP cASE
# link: https://www.hackerrank.com/challenges/swap-case/problem

""""
Task
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):
    s1 = list(s) # turns string into list of characters
    a = 0 
    
    for i in s1:
        if ord(i) > 64 and ord(i) < 91: # checks if character is uppercase
            s1[a] = i.lower()
        else: # since this command doesn't affect non-letters everything else is lowercase
            s1[a] = i.upper()
        a=a+1 # increment to next character
    s2="".join(s1) # turns back into string
    return s2 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
