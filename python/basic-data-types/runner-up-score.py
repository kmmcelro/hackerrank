# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Find the Runner-Up Score!
# link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

""""
Task
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # initializing the variables to track winner and runner-up scores
    y1 = arr[0] 
    y2 = arr[0]
    
    for a in arr:
        # in case the first term is the highest score this will make sure the runner-up flag gets set to a lower value in the list
        if y1 == y2 and a < y2: 
            y2 = a 
        # checking values in the list that are higher than the current second highest and resetting flags (y1, y2) by a's value relative to the flags
        elif (a > y2):
            if (a > y1):
                y2 = y1
                y1 = a
            elif(a != y1):
                y2 = a
print(y2)