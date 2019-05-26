"""Given an array of n integers. The task is to print
the duplicates in the given array. If there are no duplicates then print -1"""


def printDup(arr):
    n=len(arr)
    d_arr = {}
    for ele in arr:
        try:
            d_arr[ele]+=1
        except:
            d_arr[ele]=1

    for item in d_arr:
        if d_arr[item]>1:
            print("%d"%(item),end=" ")

if __name__ == "__main__":
    list = [12, 11, 40, 12,
            5, 6, 5, 12, 11]
    printDup(list)


