"""Given an array of n elements such that elements may repeat.
We can delete any number of elements from array. The task is to find minimum
number of elements to be deleted from array to make it equal."""

from collections import Counter

def minDelte(arr):
    n=len(arr)

    d_arr = Counter(arr)

    return n - d_arr.most_common(1)[0][1]

arr = [4, 3, 4, 4, 2, 4]

print("Count of pairs is", minDelte(arr))
