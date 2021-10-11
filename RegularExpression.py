import re
from typing import Pattern

# function for the sequence of digits
def getdigits(phrase):
    output = re.findall(r'[0-9]+',phrase)
    return output

# function for the sequence of non-digits
def getnondigits(pattern,phrase):
    for p in pattern:
        match = re.findall(p, phrase)
        return match

# function for the sequence of whitespace
def getwhitespace(space, phrase):
    for sp in space:
        match = re.findall(sp, phrase)
        return match

# function for the sequence of non-whitespace
def getnowhitespace(nospace, phrase):
    for ns in nospace:
        match = re.findall(ns, phrase)
        return match

# function for the sequence of Alphanumeric
def getAlphanumeric(alpha, phrase):
    for an in alpha:
        match = re.findall(an, phrase)
        return match

# function for the sequence of non-Alphanumeric
def getnonAlphanumeric(nonalpha, phrase):
    for na in nonalpha:
        match = re.findall(na, phrase)
        return match


phrase = 'This is a string and it has some numbers like 5533 and a symbol #hashtag'
Pattern = [r'\D+'] #Sequence of digits
space = [r'\s']    #Sequence of non-digits
nospace = [r'\S'] #Sequence of whitespace
alpha = [r'\W']   #Sequence of non-whitespace
nonalpha = [r'\w'] #non alphanumeric

# print Sequence of digits
output = getdigits(phrase)
print(*output)

# print Sequence of non-digits
match = getnondigits(Pattern,phrase)
print(*match)

#print Sequence of whitespace
match= getwhitespace(space, phrase)
print(*match)

# print Sequence of non-whitespace
match = getnowhitespace(nospace, phrase)
print(*match)

# print Sequence of non-whitespace
match = getAlphanumeric(alpha, phrase)
print(*match)

# print non alphanumeric
match = getnonAlphanumeric(nonalpha, phrase)
print(*match)




