def alphabetize(thisString):
    newString = ''
    newString.join(sorted(thisString))
    return newString

def anagram(aString, bString):
    if len(aString) != len(bString):
        return False
    aString = alphabetize(aString)
    bString = alphabetize(bString)
    if aString == bString:
        return True
    else:
        return False

a = anagram("dad","add")
print a

a = anagram("bad","add")
print a

a = anagram("ddad","add")
print a

a = anagram("ohmygodicantbelieveit","ogeodilycantbmievheit")
print a

a = anagram("herp","suckit")
print a

a = anagram("david","divad")
print a
