my_list = ["geeks", "geeg", "keek", "practice", "aa"]

result = list(filter(lambda x:(x=="".join(reversed(x))),my_list))
#result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
print(result)