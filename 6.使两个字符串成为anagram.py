from collections import Counter

def makeAnagram(str1,str2):
    c1 = Counter(str1)
    c2 = Counter(str2)

    c3 = c1&c2

    n1 = len(list(c1.elements()))
    n2 = len(list(c2.elements()))
    if len(list(c3))==0:
        return n1+n2
    else:
        return max(n1,n2) - len(list(c3.elements()))

if __name__ == "__main__":
    str1 ='cddgk'
    str2 ='gcd'
    print(makeAnagram(str1, str2))
