# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Time Delta
# link: https://www.hackerrank.com/challenges/python-time-delta/problem

""""
Task
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. 
Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. 
You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime 


def time_delta(t1, t2):
    pattern = "%a %d %b %Y %H:%M:%S %z" # defining the pattern for converting to a datetime variable
    time1 = datetime.strptime(t1, pattern).timestamp()
    time2 = datetime.strptime(t2, pattern).timestamp()
    diff = str(int(abs(time1-time2)))
    return diff

if __name__ == '__main__':
    x = 0
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
