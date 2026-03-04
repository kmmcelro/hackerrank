# Author: kmmcelro
# This is my solution to the Hackerrank challenge, Collections.OrderedDict()
# link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

""""
Task
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

"""

from collections import OrderedDict
import re

Ordered_Dict = OrderedDict()

numItems = int(input())


for i in range(numItems): # saving transactions in the dictionary, with items and current net price as the saved pair
    item, price = filter(None,re.split(r'(\d+)', input()))
    if Ordered_Dict.get(item) is None:
        Ordered_Dict[item] = int(price)
    else:
        Ordered_Dict[item] += int(price)
for itemName, net_price in Ordered_Dict.items(): # prints the values in the dictionary
    itemSum = itemName + str(net_price)
    print(itemSum)

