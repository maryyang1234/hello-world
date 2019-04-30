import copy
import array as a

# def rearrangeArr(arr):
#     """Rearrange array such that arr[i] >= arr[j] if i is even and
#     arr[i]<=arr[j] if i is odd and j < i"""
#     brr = []
#     for i in range(0,len(arr)):
#         brr.append(arr[i])
#
#     n = len(arr)
#     k = n//2
#     if n%2==1:
#         i=len(arr)
#         j=0
#         while i>0 and j<k+1:
#             arr[i]=brr[j]
#             i=i-2
#             j=j+1
#         i=1
#         while i<n and j<n:
#             arr[i]=brr[j]
#             i=i+2
#             j=j+1
#
#     else:
#         i=n-1
#         j=0
#         while i>0 and j<k+1:
#             arr[i]=brr[j]
#             i=i-2
#             j=j+1
#         i = 1
#         while i < n and j < n:
#             arr[i] = brr[j]
#             i = i + 2
#             j = j + 1
#
# arr = a.array('i', [ 1, 2, 3, 4, 5, 6, 7 ])
# print(rearrangeArr(arr))

import array as a
import numpy as np

def rearrangeArr(arr,n):
    evenPos = int(n/2)

    oddPos = n - evenPos

    tempArr = np.empty(n,dtype = object)

    for i in range(0,n):
        tempArr[i] = arr[i]

    tempArr.sort()

    j=oddPos-1

    for i in range(1,n,2):
        arr[i] = tempArr[j]
        j=j-1

    j = oddPos

    for i in range(1,n,2):
        arr[i] = tempArr[j]
        j=j+1

    for i in range(0,n):
        print(arr[i],end="")

arr = a.array('i', [ 1, 2, 3, 4, 5, 6, 7 ])
rearrangeArr(arr, 7)
