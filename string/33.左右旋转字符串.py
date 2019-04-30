"""Given a string of size n, write functions to perform
following operations on string.

Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
Right (Or clockwise) rotate the given string by d elements (where d <= n)."""

def rotate(input,d):
    n = len(input)
    Left = input[d:]+input[0:d]
    Right = input[n-d:n] + input[0:n-d]

    print("Left rotate %d elements"%(d),Left)
    print("Right rotate %d elements"%(d),Right)

if __name__ == "__main__":
    input = 'GeeksforGeeks'
    d=2
    rotate(input,d)

