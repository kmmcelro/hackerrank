# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Designer Door Mat
# link: https://www.hackerrank.com/challenges/designer-door-mat/problem

""""
Task

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""

n, m = map(int, input().split(" "))

dotline = ".|." # making the pattern characters into strings 
dash = "-"
dashm = (m - 3) // 2
if (n % 2) == 1:
    if (m % n) == 0 and (m / n) == 3:
        for i in range(0, n // 2): # top half of mat
            totdash = dash * (dashm - 3*i)
            totdotline = dotline*(1 + 2*i)
            line = totdash + totdotline + totdash 
            print(line)
        nweldash = (m - 7) // 2
        welcome = dash*nweldash + "WELCOME" + dash*nweldash #middle line
        print(welcome) 
        for i in range((n // 2 - 1), -1, -1): # bottom half of mat
            totdash = dash * (dashm - 3*i)
            totdotline = dotline*(1 + 2*i)
            line = totdash + totdotline + totdash 
            print(line)
            #could turn the stuff in the for loop into a function that's called instead of repeating
    else: # protection against wrong inputs
        print("The second number is not 3 times the first number.\n")
else:
    print("The first number needs to be odd.\n")