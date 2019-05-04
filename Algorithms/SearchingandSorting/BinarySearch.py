"""Search a sorted array by repeatedly dividing the search interval in
half. Begin with an interval covering the whole array. """

def BinSea(arr,x,l,n):

    mid =(l+n)//2

    if l==n and arr[l]!=x:
        return -1

    if arr[mid]==x:
        return mid
    elif arr[mid]<x:
        return BinSea(arr,x,mid,n)
    else:
        return BinSea(arr,x,l,mid)

def BinSea2(arr,x,l,n):

    mid = (l+n)//2

    while(l<=n):
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid+1
            mid=(l+n)//2
        else:
            n=mid-1
            mid=(l+n)//2
    return -1







arr=[1,3,4,23,34,56,78,90]
n=len(arr)
x=23
l=0

result = BinSea2(arr,x,l,n)

print("the index of %d is %d(-1 means can't find the number)"%(x,result))

