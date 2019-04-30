"""Given two strings, check if s1 is there in s2."""

def checkStr(str1,str2):

    if (str2.find(str1)==-1):
        print("No")
    else:
        print("Yes")

string = "geeks for geeks"
sub_str ="geek"
checkStr( sub_str,string)