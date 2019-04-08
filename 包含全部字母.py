"""Given a string, check if the given string is pangram or not."""

def panagram(str):
    set_pan = set("abcdefghijklmnopqrstuvwxyz")

    str.lower()

    for i in str:
        if i in set_pan:
            set_pan.remove(i)

    if set_pan == set():
        print("The string is a pangram")
    else:
        print("The string isn't a pangram")

strng ="The quick brown fox jumps over the lazy dog"
panagram(strng)