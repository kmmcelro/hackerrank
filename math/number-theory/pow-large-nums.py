# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Power of large numbers
# link: https://www.hackerrank.com/challenges/power-of-large-numbers/problem

""""
Task
The city of Hackerland has formed a new football club and wants to participate in the upcoming Football League of their country. 
The coach is worried that they will not be able to qualify because they don't have a famous footballer in their team. 
The assistant coach suggests that the team should buy Cristiano Ronaldo as he can single-handedly get their team qualified.

On day 1, today, the club has to pay 'A' HackerCoins in order to buy Ronaldo. 
After each passing day, the price of buying Ronaldo becomes A times the price on the previous day. 
Any normal person would buy him on the 1st day itself as the price will be the lowest but since the coach always failed in high school Mathematics, he wants 'B' days to think before making him an offer.

As the coach doesn't know how to calculate the price of Ronaldo on the Bth day, he has asked for your help.

Your task is to tell the price of Ronaldo on the Bth day. Since, the price can be a very large number, please tell him the price modulo 10^9 + 7.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def solve(a, b):
    # Write your code here
    mod = 10**9 + 7
    a1 = 0
    for ach in a:
        a1 = (a1 * 10 + int(ach)) % mod # handling large values of a by converting each decimal place individually
    result = 1
    for bch in b:
        result = (pow(result, 10, mod) * pow(a1, int(bch), mod)) % mod # handling large values of b by doing the operation for each decimal place individually
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = first_multiple_input[0]

        b = first_multiple_input[1]

        result = solve(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
