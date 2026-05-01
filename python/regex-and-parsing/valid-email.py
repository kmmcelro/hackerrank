# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Validating and Parsing Email Addresses
# link: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

""""
Task
A valid email address meets the following criteria:

* It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
* The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
* The domain and extension contain only English alphabetical characters.
* The extension is 1, 2, or 3 characters in length.

Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

"""

import re
import email.utils


sPattern = re.compile(r'^[a-zA-Z]{1}[a-zA-Z0-9_.-]+@[a-zA-Z]+\.+[a-zA-Z]{1,3}$')

n = int(input())

for i in range(0,n):
    # could have put immediately converted input and used formataddr to convert back to input format, but it's unnecessary here
    s = input()
    name, address = email.utils.parseaddr(s) 
    if sPattern.match(address):
        print(s)
