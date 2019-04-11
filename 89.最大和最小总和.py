"""Given two positive numbers calculate the minimum and
maximum possible sums of two numbers. We are allowed to replace
digit 5 with digit 6 and vice
versa in either or both the given numbers."""


def replaceDig(x,from1,to):
    result = 0
    remainder = 1

    while(x%10>0):
        re = x%10

        if(re == from1):
            result=result+to*remainder
        else:
            result=result +re *remainder

        remainder=remainder*10
        x=int(x/10)
    return result

def calculateMinMaxSum(x1, x2):

    minsum = replaceDig(x1,6,5)+replaceDig(x2,6,5)
    maxsum = replaceDig(x1,5,6)+replaceDig(x2,5,6)

    print("the minsum of changed x1 and a2 is :", minsum)
    print("the maxsum of changed x1 and a2 is :", maxsum)

if __name__=='__main__':
    x1 = 5466
    x2 = 4555
    calculateMinMaxSum(x1, x2)


