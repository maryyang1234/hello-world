import re

def findSum(str1):
    p = re.compile("[0-9]+")
    list = p.findall(str1)
    sum  =0
    for i in list:
        sum= sum+int(i)

    return sum


str1 = "12abc20yz68"
print(findSum(str1))

"""def find_sum(str1): 
    # Regular Expression that matches digits in between a string 
    return sum(map(int,re.findall('\d+',str1))) """