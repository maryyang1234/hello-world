def findMax1(str1):
    print(max(map(len,input.split('0'))))


input = '11000111101010111'
findMax1(input)

# input.split('0') --> splits all sub-strings of consecutive 1's
# separated by 0's, output will be like ['11','1111','1','1','111']
# map(len,input.split('0'))  --> map function maps len function on each
# sub-string of consecutive 1's
# max() returns maximum element from a list


