# Author: kmmcelro
# This is my solution to the Hackerrank challenge, No Idea!
# link: https://www.hackerrank.com/challenges/no-idea/problem

""""
Task
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. 
Your initial happiness is 0. 
For each i integer in the array, if i ∈ A, you add 1 to your happiness. 
If i ∈ B, you add -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

"""

n, m = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

happiness = 0
for elem in array:
    if elem in A:
        happiness += 1
    elif elem in B:
        happiness -= 1
        
print(happiness)