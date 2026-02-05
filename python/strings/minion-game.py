# Author: kmmcelro
# This is my solution to the Hackerrank challenge, The Minion Game
# link: https://www.hackerrank.com/challenges/the-minion-game/problem

""""
Task
Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.
"""

def minion_game(string):
    vowels = 'AEIOU'
    Kevin_Score = 0
    Stuart_Score = 0
    for i in range(len(string)):
        substring = string[i] 
        if vowels.find(substring) > -1: # checks if current char is a vowel for Kevin's score
            Kevin_Score += len(string) - i
        else: # consonants go to Stuart
            Stuart_Score += len(string) - i
    if Kevin_Score > Stuart_Score:
        print("Kevin " + str(Kevin_Score))
    elif Kevin_Score < Stuart_Score:
        print("Stuart " + str(Stuart_Score))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)