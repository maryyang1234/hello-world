"""Given an IP address, remove leading zeros from the IP address."""

def deleteZero(str):
    str_list = list(str.split("."))
    for j in range(0,len(str_list)):
        zero = 0
        sub_str_list = []
        for  i in str_list[j]:
            if i!='0':
                zero = 1
                sub_str_list.append(i)
            elif i=="0" and zero !=0:
                sub_str_list.append(i)
        str_list[j] = "".join(sub_str_list)

    print(".".join(str_list))

ip ="100.020.003.400"
deleteZero(ip)


# def removeZeros(ip):
#     # splits the ip by "."
#     # converts the words to integeres to remove leading removeZeros
#     # convert back the integer to string and join them back to a string
#     new_ip = ".".join([str(int(i)) for i in ip.split(".")])
#     return new_ip;
#



