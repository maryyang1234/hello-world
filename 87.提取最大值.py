import re

def findMax(str1):
    p = re.compile("\d+")
    return max(map(int,p.findall(str1)))

str1 = "100klh564abc365bg"
print(findMax(str1))
