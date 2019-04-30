"""Given two strings string1 and string2,
the task is to find the smallest substring in string1
containing all characters of string2 efficiently."""
from collections import Counter



def min_window(str,pattern):

    missing = len(pattern)

    need = Counter(pattern)

    I=J=i=0

    for j,ele in enumerate(str,1):

        missing-=need[ele]>0
        need[ele]-=1

        if not missing :
            while need[str[i]]<0:
                need[str[i]]+=1
                i+=1

            if not J or j-i<=J-I:
                I,J=i,j

            need[str[i]]+=1
            missing+=1
            i+=1

    return str[I:J]

str = "this is a test string"
pat = "tist"
print(min_window(str,pat))






