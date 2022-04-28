testString = '   String for replacing spaces TEST   '
noLeadingWhitespace = testString.lstrip()
noTrailingWhitespace = testString.rstrip()
noLeadingOrTrailingWhitespace = testString.strip()
replaceSpaceString = testString.replace(' ', '-')
print(noLeadingWhitespace + '-')
print(noTrailingWhitespace + '-')
print(noLeadingOrTrailingWhitespace + '-')
print(replaceSpaceString + '-')
