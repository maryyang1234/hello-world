"""Given an unsorted array arr[] and two numbers x and y, find the
minimum distance between x and y in arr[]. The array might also contain duplicates.
You may assume that both x and y are different and present in arr[]."""


def findMindis(arr,x,y):

    for i in range(0,len(arr)):
        if arr[i]==x or arr[i]==y:
            prev = i
            break
    m = 99999
    for i in range(0,len(arr)):
        mi = 9999
        if arr[i]==arr[prev]:
            prev = i
        elif arr[i]!=arr[prev] and (arr[i]==x or arr[i]==y):
            mi = i-prev
            if mi<m:
                m = mi

    return m


arr = [2, 5, 3, 5, 4, 4, 2, 3]
x = 2
y = 3
print("Minimum distance between ",x," and ", y,"is",findMindis(arr,x, y))