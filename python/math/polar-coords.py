# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Polar Coordinates
# link: https://www.hackerrank.com/challenges/polar-coordinates/problem

""""
Task
You are given a complex number z. Your task is to convert it to polar coordinates.

"""

import math 

z = complex(input())
print(abs(z))
print(math.atan2(z.imag, z.real))