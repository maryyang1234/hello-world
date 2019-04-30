"""Given a sequence of strings,
the task is to find out the second most repeated
(or frequent) string in the given sequence.
(Considering no two words are the second most repeated,
there will be always a single word)."""


from collections import Counter

def secondFre(input):

    d_input = Counter(input)

    value = sorted(d_input.values(),reverse=True)

    secondLa=value[1]

    for (key,value) in d_input.items() :
        if value ==secondLa:
            print(key)
    return

if __name__ == "__main__":
    input = ['aaa','bbb','ccc','bbb','aaa','aaa']
    secondFre(input)

