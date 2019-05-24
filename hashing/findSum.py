"""Write a program that, given an array A[] of n numbers and another number x,
 determines whether or not there exist two elements in S whose sum is exactly x."""
from collections import Counter

def hasArrayTwoCandidates(A,arr_size,sum):

    d_A = Counter(A)

    i=0
    while(i<arr_size):
        if A[i] in d_A and sum-A[i] in d_A:
            return True
        i=i+1

    return False


A = [1,4,45,6,10,-8]
n = 23
if (hasArrayTwoCandidates(A, len(A), n)):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements with the given sum")


