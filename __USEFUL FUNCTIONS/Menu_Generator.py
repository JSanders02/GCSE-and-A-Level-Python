from math import ceil

def longestOption(oList):
    longest = 5
    for i in oList:
        if len(i) > longest:
            longest = len(i)
    return longest

def spaceBefore(longest,option):
    difference = longest - len(option)
    return difference // 2

def spaceAfter(longest,option):
    difference = longest - len(option)
    return ceil(difference / 2)

def createMenu(longest, oList):
    longest += 8
    print("\n\n\nprint('''\n\n")
    print('@' * (longest + 4))
    print("@@" + " " * longest + "@@")
    print("@@" + " " * longest + "@@")
    for i in oList:
        print("@@" + " " * spaceBefore(longest, i) + i + " " * spaceAfter(longest, i) + "@@")
        print("@@" + " " * longest + "@@")
    print("@@" + " " * longest + "@@")
    print('@' * (longest + 4))
    print("\n''')")
    choiceList = [str(i) for i in range(1,len(oList) + 1)]
    print('''\nchoice = 'None'
choiceList =  ''' + str(choiceList) + '''

while choice not in choiceList:
    choice = input('Enter choice [''' + '/'.join(choiceList) + ''']: ') ''')

    for i in range(1,len(choiceList) + 1):
        print('''if choice == "''' + str(i) + '''":
    time.sleep(0.5)''')

optionList = []
option = 'None'
number = 1

while option.lower() != 'menu done':
    option = input("Enter option, or type 'Menu Done' to finish [options are numbered automatically]: ")
    if option.lower() != 'menu done':
        option = str(number) + ') ' + option
        optionList.append(option)
        number += 1

longest = longestOption(optionList)
createMenu(longest, optionList)