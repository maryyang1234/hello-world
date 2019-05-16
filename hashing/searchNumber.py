"""Given a limited range array contains both positive and non-positive numbers,
 i.e., elements are in the range from -MAX to +MAX. Our task is to search
 if some number is present in the array or not in O(1) time."""


def search(arr,n,x):
    max=1000
    has=[[0 for i in range(2)] for j in range(max+1)]
    for i in range(0,n):
        if arr[i]>=0:
            has[arr[i]][0]=1
        else:

            has[abs(arr[i])][1]=1

    if  x>=0:
        if has[x][0]==1:
            return True
        else:
            return False
    else:

        if has[abs(x)][1]==1:
            return True
        else:
            return False


a = [-1, 9, -5, -8, -5, -2]
n = len(a)
x = -5
if search(a,n,x)==True:
    print("present")
else:
    print("Not present")
