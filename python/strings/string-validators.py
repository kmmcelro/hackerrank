# Author: kmmcelro
# This is my solution to the Hackerrank challenge, String Validators
# link: https://www.hackerrank.com/challenges/string-validators/problem

""""
Task
You are given a string S.
Your task is to find out if the string S contains: 
alphanumeric characters, 
alphabetical characters, 
digits, 
lowercase and uppercase characters.
"""


if __name__ == '__main__':
    s = input()
    slist = [False, False, False, False, False] # stores whether or not there is to print later; default is false
    for char in s: # checks each individual char in string
        if char.isalnum(): # all relevant cases are alphanumeric, no reason to check anything else for the char if it isn't
            slist[0] = True
            if char.isdigit(): # checks if it's a number
                slist[2] = True
            else: # if it's not a number it's a letter
                slist[1] = True
                if char.islower(): # checks if it's lowercase
                    slist[3] = True
                else: # if it's not lowercase it's uppercase
                    slist[4] = True
                    
    for i in range(0,5): # loops over and prints the boolean values in the saved list
        print(slist[i],end='\n')
                
