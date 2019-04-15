def deleRepea(str):
    str1 = ""
    for i in range(0,len(str)-1):
        if str[i] !=str[i+1]:
            str1=str1+str[i]
    str1 = str1+str[i+1]

    return str1

# Driver program
if __name__ == "__main__":
    input = 'aabccba '
    print(deleRepea(input))

