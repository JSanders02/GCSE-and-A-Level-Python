import os
import sys
import time
import random

try:
    shell = sys.stdout.shell
    colour = True
except AttributeError:
    print("You must run this program in IDLE for colours. Program will run in colourless mode.")
    colour = False

DELAY = 0.5

##Main Menu
def menu():
    print("""

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@                             @@
    @@                             @@
    @@    1. User-created list     @@
    @@                             @@
    @@       2. Random list        @@
    @@                             @@
    @@                             @@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    """)
    choice = 'None'
    choiceList = ['1','2']

    while choice not in choiceList:
        choice = input("Enter choice [1/2]: ")
    if choice == '1':
        enterList()
    if choice == '2':
        listGenerator()
    
##List inputter
def enterList():
    stringList = []
    string = 'None'

    while string.upper() != 'STOPLIST':
        string = input("Enter string for list, or type 'stoplist' to finish the list: ")
        if string.upper() != "STOPLIST":
            stringList.append(string)
            
    insertionSort(stringList)

##Random string list
def randString(amount):
    strings = []
    for i in range(0,amount):
        string = []
        length = random.randint(1,10)
        for i in range(0,length):
            isLetter = random.randint(0,1)            
            if isLetter == 1:
                isCapital = random.randint(0,1)
                if isCapital == 1:
                    char = chr(random.randint(65,90))
                elif isCapital == 0:
                    char = chr(random.randint(97,122))
            elif isLetter == 0:
                char = chr(random.randint(48,57))
            string.append(char)

        string = ''.join(string)
        strings.append(string)
    return strings

##List Generator
def listGenerator():
    length = 'None'

    while length.isnumeric() == False:
        length = input("Enter desired number of strings in list: ")
        if length.isnumeric() == False:
            if colour:
                shell.write("Invalid input. Please enter a numerical value with no special characters.\n","stderr")
            elif not colour:
                print("Invalid input. Please enter a numerical value with no special characters.")

    toSort = randString(int(length))       
    insertionSort(toSort)

##Sort time fellas
def insertionSort(toSort):
    isSorted = False
    sortedList = [toSort[0]]
    while not isSorted:
        print(' | '.join(toSort))
        for i in toSort[1:]:
            time.sleep(DELAY)
            print('Selected item: ' + i)
            sortedListLength = len(sortedList) - 1
            for item in sortedList:
                if item.lower() < i.lower():
                    if sortedList.index(item) == sortedListLength:
                        sortedList.append(i)
                        break
                    else:
                        pass
                elif item.lower() > i.lower() or item.lower() == i.lower():
                    sortedList.insert(sortedList.index(item), i)
                    break
            time.sleep(DELAY)
            if colour:
                shell.write("Inserting...\n\n","STRING")
            elif not colour:
                print("Inserting...\n")
            time.sleep(DELAY)
            print(' | '.join(sortedList))
        isSorted = True

    time.sleep(DELAY)           
    if colour:
        shell.write("List has been sorted!\n","STRING")
    elif not colour:
        print("List has been sorted!")

menu()
