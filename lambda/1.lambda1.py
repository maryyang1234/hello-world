my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]

list1 = list(filter(lambda x: (x%13==0), my_list))

print(list1)

my_list2 = ["geeks", "geeg", "keek", "practice", "aa"]

list2 = list(filter(lambda x:(x == "".join(reversed(x))),my_list2))

print(list2)

from collections import Counter

my_list3 = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"

list3 = list(filter(lambda x: (Counter(str)==Counter(x)),my_list3))
print(list3)

my_list4 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
list4 = list(map(lambda x: x*2, my_list4))
print(list4)

from functools import reduce
my_list5 = [5, 8, 10, 20, 50, 100]
list5= reduce((lambda x, y: x + y), my_list5)
print(list5)


"""Given an array of positive and negative numbers, 
arrange them such that all negative integers appear before all 
the positive integers in the array.The order of appearance should be maintained."""

def Rearrange(lst):

    return [x for x in lst if x<0] + [x for x in lst if x>=0]


# Function to rearrange positive and negative elements
def Rearrange(arr):
    # First lambda expression returns list of negative numbers
    # in arr.
    # Second lambda expression returns list of positive numbers
    # in arr.
    return [x for x in arr if x < 0] + [x for x in arr if x >= 0]


# Driver function
if __name__ == "__main__":
    arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    print(Rearrange(arr) )

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# filter是起到一个筛选的作用，map则是将其第一个参数也就是一个函数应用到第二个参数中
# result contains odd numbers of the list
result = filter(lambda x: x % 2, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

from functools import reduce

def oddtimes(input):

    print(reduce(lambda  a,b:a^b,input))

# Driver program
if __name__ == "__main__":
    input = [1, 2, 3, 2, 3, 1, 3]
    oddtimes(input)

lis = [ 1 , 3, 5, 6, 2, ]
print(reduce(lambda a, b: a+b, lis))
print(reduce(lambda a, b : a if a > b else b, lis))

fib = lambda n: reduce(lambda x,_: x + [x[-1] + x[-2]],
                       range(n - 2), [0, 1])

print(fib(9))



