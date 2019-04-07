"""Given a 26 letter character set, which is equivalent to character
set of English alphabet i.e. (abcd….xyz) and act as a relation.
We are also given several sentences and we have to translate them with
the help of given new character set."""
# utf-8

def newString(charset,input):
    oricharset = "abcdefghijklmnopqrstuvwxyz"
    mapchars=dict(zip(charset,oricharset))

    output = [mapchars[chr] for chr in input ]

    print("".join(output))

if __name__ == "__main__":
    charSet = 'qwertyuiopasdfghjklzxcvbnm'
    input = 'utta'
    newString(charSet,input)

