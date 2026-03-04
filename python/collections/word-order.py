# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Word Order
# link: https://www.hackerrank.com/challenges/word-order/problem

""""
Task
You are given n words. Some words may repeat. 
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 

"""

from collections import OrderedDict

Ordered_Dict = OrderedDict()

numItems = int(input())

for i in range(numItems): # saving "words" and their current appearance count in the dictionary
    item = input()
    if Ordered_Dict.get(item) is None:
        Ordered_Dict[item] = 1
    else:
        Ordered_Dict[item] += 1

countList = ""
print(len(Ordered_Dict)) # printing the number of words
for value in Ordered_Dict.values():
    countList += str(value) + " " # string of number of appearances in order of when the word appears
print(countList)
