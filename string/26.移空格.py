"""Given a string that has set of words and spaces,
write a program to move all spaces
to front of string, by traversing the string only once."""


def moveWs(input):
    count = 0
    for i in input:
        if i == " ":
            count+=1
    input = "".join(input.split(" "))

    print(" "*count,input)

if __name__ == "__main__":
    input = 'move these spaces to beginning'
    moveWs(input)
