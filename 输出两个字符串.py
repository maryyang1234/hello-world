"""Given an input string str[], generate two output strings.
One of which consists of those character which occurs only
once in input string and second which consists of multi-time
occurring characters. Output strings must be sorted."""

from collections import Counter

def  outTwoString(str):
    dict = Counter(str)

    once = [key for (key,count) in dict.items() if count==1]

    rep = [key for (key,count) in dict.items() if count>1]

    once.sort()
    rep.sort()
    print("".join(once))
    print("".join(rep))

if __name__ == "__main__":
    input = "geeksforgeeks"
    outTwoString(input)