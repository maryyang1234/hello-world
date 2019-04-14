
"""Calculate difficulty of a given sentence. Here a Word i
s considered hard if it has 4 consecutive consonants or number of
consonants are more than number of vowels. Else word is easy.
Difficulty of sentence is defined as 5*(number of hard words) + 3*(number of easy words)."""
from collections import  Counter

def isVowels(chr):
    chr1 = chr.lower()
    if chr1 == 'a'or chr1 == 'e' or chr1 == 'i' or chr1 == 'o' or chr1 == 'u':
        return True
    else:
        return False

def isHard(word):
    c = 0
    v = 0

    for chr in word:
        if isVowels(chr)==False:
            c += 1
        else:
            v += 1
    if c > v:
        return True


    i = 0
    while i <len(word)-4:
        if isVowels(word[i])==False :
            i+=1
            if  isVowels(word[i])==False:
                i+=1
                if isVowels(word[i])==False:
                    i+=1
                    if isHard(word[i]) == False:
                            return True
    return False

def calcDiff(str):
    l_str = str.split(" ")

    h = 0
    e = 0
    for i in range(0,len(l_str)):
        if isHard(l_str[i])==True:
            h+=1
        else:
            e+=1

    print("Diffculty of the sentence is : ",5 * h+3*e)

if __name__=="__main__":
    str = "Difficulty of sentence"
    str2 = "We are geeks"
    calcDiff(str)
    calcDiff(str2)


