#include <stdio.h>
#include <stdlib.h>

int LinearSea(int arr[],int x, int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        if(arr[i] == x)
        {
            return i;
        }
    }
    return -1;
}


int main()
{
    int arr[] = {23,1,5,67,15,89,};
    int n = sizeof(arr)/sizeof(arr[0]);
    int x=67;
    if(LinearSea(arr,x,n)==-1)
    {
        printf("no match!");
    }
    else printf("the index of %d is %d",x,LinearSea(arr,x,n));


    return 0;
}
