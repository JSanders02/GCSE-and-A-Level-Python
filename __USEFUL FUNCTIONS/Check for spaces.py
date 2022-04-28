def spaceCheck(string):
    string = list(string)
    newString = []
    for i in string:
        if i == ' ':
            #i == '' TO REMOVE SPACE
            #i == '-'TO SET SPACE AS OTHER (FOR EXAMPLE A HYPHEN)
            #return True IF USING FOR AN INPUT CHECKER SYSTEM
            i = '-'
        newString.append(i)
    return ''.join(newString)

String = input('Enter string to check for spaces: ')
print(spaceCheck(String))