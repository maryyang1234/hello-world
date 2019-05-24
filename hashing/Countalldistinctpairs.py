"""Given an integer array and a positive integer k, count
 all distinct pairs with difference equal to k."""
from collections import Counter

def coundisPairs(arr,arrlength ,k):

    d_arr = Counter(arr)

    pairs = 0
    for i in range(0, arrlength):
        if arr[i]-k in d_arr:
            pairs += 1
        if arr[i]+k in d_arr:
            pairs += 1
        d_arr.pop(arr[i])

    return pairs

if __name__=='__main__':
    arr = [8, 12, 16, 4, 0, 20]
    n = len(arr)
    k = 4
    print("Count of pairs with given diff is ", coundisPairs(arr, n, k))

