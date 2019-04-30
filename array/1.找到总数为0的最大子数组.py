def maxlen(arr):
    n = len(arr)
    maxsub = 0
    for i in range(0,n):


        sum=0
        max_so_far=0
        for j in range(i,n):
            sum=sum+arr[j]
            max_so_far=max_so_far+1
            if sum==0 and max_so_far>maxsub:
                maxsub=max_so_far

    return maxsub

arr = [15, -2, 2, -8, 1, 7, 10, 13]

print("Length of the longest 0 sum subarray is %d" % maxlen(arr))
