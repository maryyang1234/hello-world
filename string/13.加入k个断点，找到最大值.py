"""Given a large number as string s and an integer k which denotes the
number of breakpoints we must put in the number k <= string length.
The task is to find maximum segment value after putting exactly k breakpoints."""

def findMaxSegments(str,k):
    l_str = []
    for i in str:
        l_str.append(int(i))

    while k>0:
        n=len(l_str)
        if l_str[0]<=l_str[n-1]:
            l_str.pop(0)
        else:
            l_str.pop()
        k-=1
    sum=0
    for i in range(0,len(l_str)):
        sum=sum*10+l_str[i]

    return sum

if __name__ == '__main__':
    s = '2378356993'
    k = 3
print('Maximum number = ', findMaxSegments(s, k))



