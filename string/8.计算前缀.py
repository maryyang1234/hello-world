"""Given a string, print and count all prefixes in which first
alphabet has greater frequency than second alphabet.
Take two alphabets from the user and compare them.
The prefixes in which the alphabet given first has greater frequency
than the second alphabet, such prefixes are printed, else the result will be 0."""

def prefix(str,alp1,alp2):
    count = 0
    count1 = 0
    count2 = 0
    bigger = 0

    for i in str:
        count+=1
        if i == alp1:
            count1+=1
        elif i==alp2:
            count2+=1


        if count1>count2 :
            bigger +=1
            print(str[0 : count ])
    if bigger == 0:
        print(-1)
    else:
        print(bigger)

prefix("geek", "k", "e")