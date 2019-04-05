"""Given a string and a number N, we need to mirror the characters from
N-th position up to the length of the string in the alphabetical order.
 In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on."""

def mirrorString(str,k):


    origi = "abcdefghijklmnopqrstuvwxyz"
    reverse = 'zyxwvutsrqponmlkjihgfedcba'

    dictchars = dict(zip(origi,reverse))

    prefix = str[0:k-1]
    suffix = str[k-1: ]
    mirror = ''

    for i in range(0,len(suffix)):
        mirror = mirror + dictchars[suffix[i]]

    print(prefix + mirror)

if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorString(input, k)

