"""Given two strings, find if we can make first string from second by deleting
some characters from second and rearranging remaining characters."""
from collections import Counter

def findPossi(str1,str2):
    str_fir = Counter(str1)
    str_sec = Counter(str2)

    result = str_fir&str_sec

    return result==str_fir

if __name__ == "__main__":
    str1 = 'ABHISHEKsinGH'
    str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
    if (findPossi(str1,str2)==True):
        print("Possible")
    else:
        print("Not Possible")

