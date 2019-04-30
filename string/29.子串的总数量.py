"""Find total number of non-empty substrings of a string with N characters.
Here we use the word proper because we do
not consider string itself as part of output."""


def allSub(str):

    i=1
    list = []
    while i<len(str):
        j=0
        while j<len(str)-i+1:
            list.append(str[j:j+i])
            j+=1
        i+=1
    print(len(list))

str = "abcd"
allSub(str)