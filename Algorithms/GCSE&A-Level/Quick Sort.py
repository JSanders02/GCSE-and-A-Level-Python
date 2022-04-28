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
    numberList = []
    number = 'None'

    while number.isnumeric() == False and number.upper != 'STOP':
        number = input("Enter number for list, or type 'STOP' to finish list: ")
        if number.isnumeric() == False and number.upper != 'STOP':
            if colour:
                shell.write("Invalid input. Please enter a numerical value with no special characters.\n","stderr")
            elif not colour:
                print("Invalid input. Please enter a numerical value with no special characters.")
        elif number.isnumeric() == True:
            numberList.append(number)
            
    quickSort(numberList)

##List Generator
def listGenerator():
    length = 'None'

    while length.isnumeric() == False:
        length = input("Enter desired length of list: ")
        if length.isnumeric() == False:
            if colour:
                shell.write("Invalid input. Please enter a numerical value with no special characters.\n","stderr")
            elif not colour:
                print("Invalid input. Please enter a numerical value with no special characters.")

    numList = []

    for i in range(0,int(length)):
        number = random.randint(0,int(length) * 10)
        numList.append(number)
    quickSort(numList)

##Sort time fellas
def quickSort(toSort):

    if len(toSort) % 2 == 0:
        pivotPoint = (len(toSort) // 2) - 1
    else: 
        pivotPoint = (len(toSort) // 2)
    pivot = toSort[pivotPoint]
    endIndex = len(toSort) - 1
    toSort[pivotPoint], toSort[endIndex] = toSort[endIndex], toSort[pivotPoint]

    leftBound = 0
    rightBound = endIndex - 1

    while rightBound >= leftBound:

        while toSort[leftBound] < pivot:
            leftBound += 1

        while toSort[rightBound] >= pivot and rightBound >= leftBound:
            rightBound -= 1

        if rightBound >= leftBound:
            toSort[leftBound], toSort[rightBound] = toSort[rightBound], toSort[leftBound]

    toSort[endIndex], toSort[leftBound] = toSort[leftBound], toSort[endIndex]
    leftList = toSort[:leftBound]
    rightList = toSort[leftBound + 1:]

    if leftBound > 0:
        quickSort(leftList)
        toSort[:leftBound] = leftList
    if len(toSort[leftBound + 1:]) > 1:
        quickSort(rightList)
        toSort[leftBound + 1:] = rightList

    print('List/Sublist sorted: ' + ' | '.join([str(i) for i in toSort]))
menu()
