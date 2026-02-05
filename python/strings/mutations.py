# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Mutations
# link: https://www.hackerrank.com/challenges/python-mutations/problem

""""
Task
You are given an immutable string, and you want to make changes to it.
Read a given string, change the character at a given index and then print the modified string.
"""

def mutate_string(string, position, character):
    position2 = position + 1
    string = string[:position] + character + string[position2:] # all characters before position + changed character + all characters after position
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)