import re
#                   👇这里有一个空格
regex = r"([a-zA-z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:
    # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    #    match.group(0) always returns the fully matched string
    #    match.group(1) match.group(2), ... return the capture
    #    groups in order from left to right in the input string
    #    match.group() is equivalent to match.group(0)
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group(0)))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)) )
else:
    print("The regex pattern does not match.")

# def findMonthAndDate(string):
#     regex= r"([a-zA-Z]+) (\D+)"
#     match = re.match(regex,string)
#     if match == None:
#         print("Not a valid date")
#         return
#     print( "sec","Given Date:%s" % (match.group()))
#     print("Month:%s" % (match.group(1)))
#     print("Day: %s" % (match.group(2)))
#
# findMonthAndDate("Jun 24")
# print("")
# findMonthAndDate("I was born on June 24")

def findMonthAndDate(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)

    if match == None:
        print("Not a valid date")
        return

    print("Given Data: %s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))

# Driver Code
findMonthAndDate("Jun 24")
print("")
findMonthAndDate("I was born on June 24")
