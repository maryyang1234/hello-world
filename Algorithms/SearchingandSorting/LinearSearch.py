"""Given an array arr[] of n elements,
write a function to search a given element x in arr[]."""

def LinearSea(arr,x,n):
    """arr is a array to find x,
    n is the length of arr"""

    for i in range(0,n):
        if arr[i]==x:
            return i

    return -1

arr = [9,5,112,13,78,5,43]
n = len(arr)
x=13
print(LinearSea(arr,x,n))

