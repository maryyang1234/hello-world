"""You are given an array of characters which is basically a sentence.
However there is no space between different words and
the first letter of every word is in uppercase.
You need to print this sentence after following amendments:
(i) Put a single space between these words.
(ii) Convert the uppercase letters to lowercase."""
import re

def insideWs(str):
    regex = r"[A-Z][a-z]*"
    match = re.findall(regex,str)
    result = []
    for word in match:
        word = chr(ord(word[0])+32)+word[1:]
        result.append(word)
    print(" ".join(result))

if __name__ == "__main__":
    input = 'BruceWayneIsBatman'
    insideWs(input)