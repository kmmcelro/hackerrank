# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Validating Credit Card Numbers
# link: https://www.hackerrank.com/challenges/validating-credit-card-number/problem

""""
Task
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

"""

import re

creditPattern1 = re.compile(r'^[4-6][0-9]{3}+-[0-9]{4}+-[0-9]{4}+-[0-9]{4}$') # checks the dash case
creditPattern2 = re.compile(r'^[4-6][0-9]{15}$') # checks the no dash case
repeatPattern = re.compile(r'(\d)(?:-?\1){3,}') # checks for repeating digits
n = int(input())


for i in range(0,n):
    creditNum = input()
    if re.search(repeatPattern, creditNum) is not None:
        print("Invalid")
    elif creditPattern1.match(creditNum) or creditPattern2.match(creditNum):
        print("Valid")
    else:
        print("Invalid")
