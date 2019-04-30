"""Two strings are given and you have to
modify 1st string such that all the common
characters of the 2nd strings have to be removed and the uncommon
characters of the 2nd string have to be concatenated
with uncommon characters of the 1st string."""




def outNoRepeat(str1,str2):
    s_str1 = set(str1)
    s_str2 = set(str2)

    common = list(s_str2 & s_str1)
    result = [chr for chr in s_str1 if chr not in common]+ \
        [chr for chr in s_str2 if chr not in common]

    print("".join(result))


if __name__ == "__main__":
    str1 = 'aacdb'
    str2 = 'gafd'
    outNoRepeat(str1,str2)
