"""Given a string of numbers, the task is to find the maximum
value from the string, you can add a ‘+’ or ‘*’ sign between any two numbers."""


def calCulate(str):

    l_str = []
    for chr in str:
        l_str.append(int(chr))

    while min(l_str)==0:
        l_str.remove(0)

    while min(l_str)==1:
        l_str.remove(1)
        s = min(l_str)
        l_str.remove(s)
        l_str.append(s+1)
    sum = 1
    for i in range(0,len(l_str)):
        sum = sum*l_str[i]

    return sum

if __name__== "__main__":
    str = "21119";
    print(calCulate(str));