"""Given a string, find the smallest window length with all distinct
characters of the given string. For eg. str = “aabcbcdbca”,
then the result would be 4 as of the smallest window will be “dbca” ."""
from collections import Counter


def findMin(str):

    set_str = set(str)
    d_str = Counter(set_str)
    missing = len(d_str)

    I=J=i= 0

    for j ,ele in enumerate(str,1):
        missing -= d_str[ele]>0
        d_str[ele]-=0

        if not missing :
            while d_str[str[i]]<0:
                d_str[str[i]]+=1
                i+=1

            if  not J or j-i<=J-I:
                I,J = i,j

            d_str[str[i]]+=1
            missing+=1
            i+=1

    return str[I:J]

str = "aabcbcdbca"
print(findMin(str))