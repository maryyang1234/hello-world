"""Given a string of lowercase alphabets and a number k,
the task is to print the minimum value of the string after
removal of ‘k’ characters. The value of a string is defined
as the sum of squares of the count of each distinct character.
For example consider the string “saideep”, here frequencies
of characters are s-1, a-1, i-1, e-2, d-1, p-1 and value of
the string is 1^2 + 1^2 + 1^2 + 1^2 + 1^2 + 2^2 = 9."""
from collections import Counter
from queue import PriorityQueue

def minStringValue(str,k):

    if len(str)<=k:
         return 0

    d_str = Counter(str)

    q = PriorityQueue()
    for key in d_str.keys():
        q.put(-d_str[key])

    while k>0:
        temp = q.get()
        temp = temp+1
        q.put(temp,temp)
        k=k-1

    result = 0
    while not q.empty():
        temp = q.get()
        temp = temp*(-1)
        result +=temp*temp

    return result


if __name__ == "__main__":
    str = "aaabccddd"
    k = 2
    print(minStringValue(str, k))

    str = "aaab"
    k = 2
    print(minStringValue(str, k))





