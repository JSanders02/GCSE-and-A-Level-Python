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
    @@     1. Generate List        @@
    @@                             @@
    @@                             @@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    """)
    choice = 'None'
    choiceList = ['1']

    while choice not in choiceList:
        choice = input("Enter choice [1]: ")
    if choice == '1':
        listGenerator()

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
        number = random.randint(0,9999)
        numList.append(number)
    radixSort(numList, 1)

##Sort time fellas
def radixSort(toSort, passNum):
    if passNum > 1:
        print('Sorted by digit ' + str(passNum - 1) + ' (From end): ' + ' | '.join([str(i) for i in toSort]))

    if passNum <= 4:
        countList = [0,0,0,0,0,0,0,0,0,0]
        sortedList = ['' for i in toSort]

        for i in toSort:
            try:
                currentDigit = int(str(i)[-passNum])
            except IndexError:
                currentDigit = 0
            countList[currentDigit] += 1

        countList[0] -= 1

        for index in range(1,10):
            countList[index] += countList[index - 1]

        toSort.reverse()
        for i in toSort:
            try:
                currentDigit = int(str(i)[-passNum])
            except IndexError:
                currentDigit = 0
            index = countList[currentDigit]
            countList[currentDigit] -= 1
            sortedList[index] = i

        passNum += 1
        radixSort(sortedList, passNum)

menu()
