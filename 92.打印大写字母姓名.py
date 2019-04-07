"""Given a name, print the initials of a name(uppercase) with
last name(with first alphabet in uppercase) written in full separated by dots."""

def UpperName(name):
    li_name = list(name.split(" "))
    n = len(li_name)
    for i in range(0,n-1):
        s = li_name[i]
        li_name[i] = s[0].upper()

    h=li_name[n-1]
    h.title()
    li_name[n-1]=h.title()
    Newname = ".".join(li_name)
    return Newname
s ="mohandas karamchand gandhi"
print(UpperName(s))

