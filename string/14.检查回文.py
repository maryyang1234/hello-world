"""Given two strings s1 and s2,
check if both the strings are anagrams of each other."""
from collections import Counter

def anagram(str1,str2):
    d_str1 = Counter(str1)
    d_str2 = Counter(str2)

    if d_str1 == d_str2:
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams")

s1 ="listen"
s2 ="silent"
anagram(s1,s2)

