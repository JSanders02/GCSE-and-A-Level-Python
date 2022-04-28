def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

string = 'one'
while string.upper() != 'NO':
    string = input("Enter string to check if it is a float: ")

    if isFloat(string) == True:
        print('Yes')

    elif isFloat(string) == False:
        print('No')
