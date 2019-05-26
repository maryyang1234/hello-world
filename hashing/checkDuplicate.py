"""Given an unsorted array that may contain duplicates.
Also given a number k which is smaller than size of array.
Write a function that returns true if array contains duplicates within k distance."""
from collections import Counter


def checkDup(arr,k):
     d_arr = Counter() #d_arr用于保存只有k个元素的字典

     for i in range(0,k):
         d_arr[arr[i]]=1

     n=len(arr)
     for j in range(k,n):
         if arr[j] in d_arr.keys():
             return True
         else:
             d_arr.pop(arr[j-k])
             d_arr[arr[j]]=1

     return False


if __name__ == "__main__":

    arr = [10, 5, 3, 4, 3, 5, 6]
    if (checkDup(arr,3)):
        print("Yes")
    else:
        print("No")

