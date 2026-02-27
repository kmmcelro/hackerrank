# Author: kmmcelro
# This is my solution to the Hackerrank challenge, collections.counter()
# link: https://www.hackerrank.com/challenges/collections-counter/problem

""""
Task
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""

from collections import Counter

num = int(input())
myList = list(map(int, input().rstrip().split())) 

myCounter = Counter(myList) # initializes the counter for the collection
numCustomer = int(input())
total = 0

for i in range(numCustomer):
    customer_Size, price = input().rstrip().split()
    if myCounter[int(customer_Size)] > 0: # checks if size is in stock
        myCounter[int(customer_Size)] -= 1 # removes from stock and adds sale price to total if in stock
        total += int(price)    
print(total)
