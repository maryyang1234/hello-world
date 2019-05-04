#include <stdio.h>
#include <stdlib.h>

int BinSea(int arr[],int x,int l, int n)
{
    int mid = (l+n)/2;

    while(l<=n)
    {


    if(arr[mid] == x)
    {
        return mid;
    }
    if(arr[mid]<x)
    {
       l=mid+1;
       mid=(l+n)/2;
    }
    else
    {
        n=mid-1;
        mid=(l+n)/2;
    }
  }
  return -1;
}

int main()
{
    int arr[]={1,3,4,23,34,56,78,90};
    int n=sizeof(arr)/sizeof(arr[0]);
    int x=23;
    int l=0;
    printf("the index of %d is %d(-1 means can't find the number)",x,BinSea(arr,x,l,n-1));
    return 0;
}
