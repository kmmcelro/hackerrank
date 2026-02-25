# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Find Angle MBC
# link: https://www.hackerrank.com/challenges/find-angle/problem

""""
Task
ABC is a right triangle, 90° at B.
Therefore, angle ABC = 90°.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find  angle MBC in degrees.

"""

from math import atan
from math import pi


AB = float(input())
BC = float(input())

theta = round(atan(AB/BC)*360/(2*pi))
print(str(theta) + "\u00b0")