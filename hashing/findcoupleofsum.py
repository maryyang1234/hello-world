"""Given an array of integers, and a number ‘sum’, find the number of pairs
 of integers in the array whose sum is equal to ‘sum’"""
from collections import Counter

def findCoupleofSum(A,arr_size,sum):

    d_A= Counter(A)

    i = 0
    coup = 0
    while(i<arr_size):
        if A[i] in d_A and sum-A[i] in d_A:
            coup = coup+1
            d_A.pop(A[i])
            d_A.pop(sum-A[i])
        i=i+1
    return coup

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      findCoupleofSum(arr, n, sum))
