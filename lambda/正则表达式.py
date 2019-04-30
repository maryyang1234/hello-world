"""\d   Matches any decimal digit, this is equivalent
     to the set class [0-9].
\D   Matches any non-digit character.
\s   Matches any whitespace character.
\S   Matches any non-whitespace character
\w   Matches any alphanumeric character, this is
     equivalent to the class [a-zA-Z0-9_].
\W   Matches any non-alphanumeric character. """


import re


p = re.compile('[a-e]')

print(p.findall("Aye, said Mr. Gibenson Stark"))


p2 = re.compile('\d')
print(p2.findall("I went to him at 11 A.M. on 4th July 1886"))

p1 = re.compile('\d+')
print(p1.findall("I went to him at 11 A.M. on 4th July 1886"))

p3 = re.compile('\w')
print(p3.findall("He said * in some_lang."))

p4 = re.compile('\w+')
print(p4.findall("I went to him at 11 A.M., he said *** in some_language."))

p5 =re.compile('\W')
print('p5',p5.findall("he said *** in some_language."))

p6 = re.compile("ab*")
print('p6',p6.findall("ababbaabbb"))

print('p7',re.split(r'\W+','Words, words, words.'))
print('p8',re.split(r'\W+', "Word's words Words"))
# print(split('\w+',"Word's words Words"))

print(re.sub('ub', '~*','Subject has Uber booked already',flags  = re.IGNORECASE))

print(re.sub('ub', '~*' , 'Subject has Uber booked already'))

print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE))

print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

# print('subn',re.subn('ub', '~*', 'Subject has Uber booked already'))
# t = re.subn('ub', '~*', 'Subject has Uber booked already uberrr', flags=re.IGNORECASE)
# print(t)
# print(len(t))
#
# # This will give same output as sub() would have
# print(t[0])

print(re.escape("This is Awseome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

