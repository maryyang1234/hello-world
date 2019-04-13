"""Given a string, write a program to count the occurrence of 
Lowercase characters, Uppercase characters, Special characters and Numeric values."""

def countChr(str):
    Upper = 0
    Lower = 0
    num = 0
    spec = 0

    for i in str:
        if i<= 'Z'and i>= 'A':
            Upper+=1
        elif i<='z' and i>='a':
            Lower+=1
        elif i<='9'and i >='0':
            num+=1
        else:
            spec +=1

    print("the number of Upper character are : ",Upper)
    print("the number of the Low character are:",Lower)
    print("the number of number character are :",num)
    print("the number of the special character are : ",spec)

str = "#GeeKs01fOr@gEEks07"
countChr(str)


