"""Given an unsorted array arr[] and two numbers x and y, find the
minimum distance between x and y in arr[]. The array might also contain duplicates.
You may assume that both x and y are different and present in arr[]."""


def findMindis(arr,x,y):
    m = len(arr)

    for i in range(0,len(arr)):
        mi = 99999
        if  arr[i] == x or arr[i] == y:
            for j in range(i, len(arr)):
                if arr[j] != arr[i] and (arr[j] == x or arr[j] == y):
                    mi = j-i
                    if mi<m:
                        m=mi

    return m

arr = [2, 5, 3, 5, 4, 4, 2, 3]
x = 2
y = 3
print("Minimum distance between ",x," and ", y,"is",findMindis(arr,x, y))



