"""Given a sorted array arr[] of size n and an element x to be searched in it.
Return index of x if it is present in array else return -1. Using Fibonacci Search"""


def fibSea(arr,x,n):
    #n 是待搜索数组arr的长度 ，x是待搜索的数，若x存在于数组中，则返回x的索引
    #若不存在，则返回-1

    fibMMm1 = 0 #初始化斐波拉契数
    fibMMm2 = 1 #初始化斐波拉契数
    fibM= fibMMm2 + fibMMm1


    #找到大于或等于n的最小斐波拉契数fibM
    while(fibM<n):
        fibMMm1=fibMMm2
        fibMMm2 = fibM
        fibM = fibMMm1 +fibMMm2

    offset = -1

    # Note that we compare arr[fibMm1] with x.
    # When fibM becomes 1, fibMm1 becomes 0
    while(fibM >1):
        #检查fibMMm1是不是有效的位置,确定下标i
        # 因为在数组中，下标是从0开始的，所以这里n-1，
        # 又因为是按照斐波拉契数来划分数组，切割点前半部分长度为fiMMm1,但是下标位置为fiMMm1-1
        i = min(offset + fibMMm1,n-1)


        #若arr[i]<x,
        if(arr[i] <x):
            fibM = fibMMm2
            fibMMm2 = fibMMm1
            fibMMm1 = fibM -fibMMm2

            offset = i
        elif(arr[i] >x):
            fibM = fibMMm1
            fibMMm2 = fibMMm2 - fibMMm1
            fibMMm1 =fibM - fibMMm2
        else:
            return i

    #offset 要么是-1，即整个数组的最小的位置0，要么是被判断过的边界的i值
    #在整个判断只剩一个元素的时候，确定这个元素的索引
    if(fibMMm2 and arr[offset +1] == x):
        return offset +1

    return -1


arr = [10, 22, 35, 40, 45, 50,
       80, 82, 85, 90, 100]
n = len(arr)
x = 85
print("Found at index:",
      fibSea(arr, x, n))



