def calcuVowel(str):
    set_vowel = set("aeiouAEIOU")
    count = 0

    for i in str:
        if i in set_vowel:
            count+=1

    return count

str = "GeeksforGeeks"
print(calcuVowel(str))


