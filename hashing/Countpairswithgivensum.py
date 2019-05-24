"""Given an array of integers, and a number ‘sum’, find
the number of pairs of integers in the array whose sum
is equal to ‘sum’."""
from collections import Counter

def countPairs(A,Alength,sum):

    d_A = Counter(A)

    coun = 0
    for i in range(0, Alength):
        coun += d_A[sum-A[i]]
        if A[i] == sum-A[i]:
            coun -= 1

    return int(coun/2)


arr = [1, 1, 1, 1]
n = len(arr)
sum = 2

print("Count of pairs is", countPairs(arr, n, sum))








