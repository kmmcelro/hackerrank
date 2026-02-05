# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Alphabet Rangoli
# link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

""""
Task
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
"""

def print_rangoli(size):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    rowNum = 2 * size - 1
    lines = []
    for i in range(size, 0,-1):
        dashnum = (i - 1) * 2
        line = dashnum * '-' # exterior dashes for each line (left side)
        curLetter = size
        while (curLetter - i > 0): # moving up the alphabet to center letter for the row 
            line += alphabet[curLetter] + '-'
            curLetter -= 1
        line += alphabet[i]
        while (curLetter < size ): # moving down the alphabet to edge letter
            curLetter += 1
            line += '-' + alphabet[curLetter]
        line += dashnum * '-' # exterior dashes for each line (right side)
        lines.append(line) #saving the lines
    for j in range(0,rowNum):
        if j < size: # counting up for rows with more letters
            print(lines[j])
        else: # counting down for symmetry
            k = rowNum - 1 - j
            print(lines[k])   

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)