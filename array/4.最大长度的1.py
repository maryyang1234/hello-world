# code
def findMax1(str1):
    a = list(map(int, str1))
    n = len(a)
    lgth_so_far = 0
    lgth = 0
    for i in range(0, n):
        if a[i] == 0:
            lgth_so_far = 0
        else:
            lgth_so_far += 1

        if lgth_so_far > lgth:
            lgth = lgth_so_far
    return lgth


if __name__ == "__main__":
    input = '11000111101010111'
    print(findMax1(input))
