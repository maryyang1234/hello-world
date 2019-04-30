"""Write a program to print all permutations of a given string"""


def toString(List,li):

#    print("".join(List), end = " ")
    return li.add("".join(List))

def permute(a,l,r,li):

    if l==r:
        toString(a,li)

    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r,li)
            a[l],a[i] = a[i],a[l]


def findMax(str1):
    n = len(str1)
    if n!=6:
        print("wrong input!")
        return
    a = list(str1)

    se = set()
    permute(a,0,n-1,se)

    a_possible = list(se)
    for  i in range(0,len(a_possible)):
        j = list(a_possible[i])
        if int(a_possible[i])>240000:
            se.remove(a_possible[i])
        elif int(j[2])>5 or int(j[4])>5:
            se.remove(a_possible[i])
    if len(se)==0:
        print("wrong input")


    ma = max(se)
    return ma




stra = "AABC"
n=len(stra)
a = list(stra)
li = set()
permute(a,0,n-1,li)
print(li)
print(findMax("294714"))




