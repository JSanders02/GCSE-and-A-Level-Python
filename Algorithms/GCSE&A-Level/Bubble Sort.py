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
            
    bubbleSort(stringList)

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
        length = input("Enter desired number of numbers in list: ")
        if length.isnumeric() == False:
            if colour:
                shell.write("Invalid input. Please enter a numerical value with no special characters.\n","stderr")
            elif not colour:
                print("Invalid input. Please enter a numerical value with no special characters.")

    numList = []

    for i in range(0,int(length)):
        number = random.randint(0,int(length) * 10)
        numList.append(number)
        
    bubbleSort(numList)

##Sort time fellas
def bubbleSort(toSort):
    maxIndex = len(toSort) - 1
    swapMade = False
    isSorted = False
    currentIndex = 0
    while not isSorted:
        for i in toSort:
            print("\n" + ' | '.join([str(i) for i in toSort]))    
            time.sleep(DELAY)            
            currentIndex = toSort.index(i)
            nextIndex = toSort.index(i)+1
            print("Selected value: " + str(i))
            if toSort.index(i) == maxIndex:
                if colour:
                    shell.write("Max index reached. Back to start.\n","ERROR")
                elif not colour:
                    print("Max index reached. Back to start.")
                break
            print("Comparing to: " + str(toSort[nextIndex]))
            if i > toSort[nextIndex]:
                if colour:
                    shell.write("Swapping...\n","STRING")
                elif not colour:
                    print("Swapping...")
                toSort[currentIndex], toSort[nextIndex] = toSort[nextIndex], toSort[currentIndex]
                swapMade = True
            else:
                if colour:
                    shell.write("No swap made.\n","stderr")
                elif not colour:
                    print("No swap made.")
        if not swapMade:
            isSorted = True
        swapMade = False
        maxIndex -= 1
    if colour:
        shell.write("List has been sorted!\n","STRING")
    elif not colour:
        print("List has been sorted!")

menu()
