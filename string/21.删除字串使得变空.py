"""Given a string “str” and another string “sub_str”.
We are allowed to delete “sub_str” from “str” any number of times.
It is also given that the “sub_str” appears only once at a time.
The task is to find if “str” can become
empty by removing “sub_str” again and again."""


# def deleteCh(str,sub_str):
#
#     if len(str)==0:
#         return False
#
#     while(len(str)!=0):
#         n=len(str)
#         index = str.find(sub_str)
#
#         if index==-1:
#             return False
#         input = str[0:index]+str[index+len(sub_str):]
#
#     return True
#
# if __name__ == "__main__":
#     input ='GEEGEEKSKS'
#     pattern ='GEEKS'
#     print(deleteCh(input, pattern))

def checkEmpty(input, pattern):
    if len(input) == 0:
        return 'false'

    while (len(input) != 0):

        # find sub-string in main string
        index = input.find(pattern)

        # check if sub-string founded or not
        if (index == (-1)):
            return 'false'

        # slice input string in two parts and concatenate
        input = input[0:index] + input[index + len(pattern):]

    return 'true'


# Driver program
if __name__ == "__main__":
    input = 'GEEGEEKSKS'
    pattern = 'GEEKS'
    print(checkEmpty(input, pattern))


