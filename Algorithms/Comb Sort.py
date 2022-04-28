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
    numList = []
    number = 'None'

    while number.upper() != 'STOPLIST' or number.isnumeric() == False:
        number = input("Enter number for list, or type 'stoplist' to finish the list: ")
        if number.upper() != "STOPLIST":
            numList.append(string)
            
    combSort(numList)

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
        
    combSort(numList)

##Sort time fellas
def combSort(toSort):
    gap = len(toSort)
    Sorted = False
    print(' | '.join([str(i) for i in toSort]))
    while not Sorted:
        try:
            for i in range(0, len(toSort)):
                print(' | '.join([str(i) for i in toSort]))
                if toSort[i] > toSort[i + gap]:
                    toSort[i], toSort[i + gap] = toSort[i + gap], toSort[i]
                    if gap == 1:
                        Sorted = True
        except IndexError:
            gap = int(gap // 1.3)
            if gap < 1:
                gap = 1
                
    if colour:
        shell.write("List has been sorted!\n","STRING")
    elif not colour:
        print("List has been sorted!")

menu()
