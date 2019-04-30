def changeChar(str,c1,c2):
    str1 = []
    for i in str:
        if i==c1:
            str1.append(c2)
        elif i==c2:
            str1.append(c1)
        else:
            str1.append(i)

    print("".join(str1))

if __name__ == "__main__":
    input = 'grrksfoegrrks'
    c1 = 'e'
    c2 = 'r'
    changeChar(input,c1,c2)

def repalceChars(str1,c1,c2):

    newchars = map(lambda x: x if (x!=c1 and x!=c2) else c1 if (x==c2) else c2,str1)
    print("".join(newchars))
if __name__ == "__main__":
    input = 'grrksfoegrrks'
    c1 = 'e'
    c2 = 'r'
    repalceChars(input,c1,c2)