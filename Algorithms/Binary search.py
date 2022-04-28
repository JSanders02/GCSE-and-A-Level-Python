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

DELAY = 1

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

    while number.upper() != 'STOP':
        number = input("Enter number for list, or type 'stop' to finish the list: ")
        if number.upper() != 'STOP' and number.isnumeric() == False:
            if colour:
                shell.write("Invalid input. Please enter a numerical value with no special characters.\n","stderr")
            elif not colour:
                print("Invalid input. Please enter a numerical value with no special characters.")

        elif number.upper() != "STOP":
            numberList.append(int(number))

    numberList.sort()

    if colour:
        shell.write("List Sorted!\n","STRING")
    elif not colour:
        print("List Sorted!")
    binarySearch(numberList)

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
    numList.sort()
    binarySearch(numList)    

##Find middle
def middle(numList):
    length = len(numList)
    middle = length // 2
    return middle - 1
    
##Search time fellas
def binarySearch(numList):
    print("List:")
    time.sleep(0.5)
    print(numList)
    
    search = 'None'

    while search.isnumeric() == False:
        search = input("Enter number to search for: ")
        if search.isnumeric() == False:
            if colour:
                shell.write("Invalid input. Please enter a numerical value with no special characters.\n","stderr")
            elif not colour:
                print("Invalid input. Please enter a numerical value with no special characters.")

    search = int(search)
    originalList = numList
    selected = 'None'

    while selected != search:
        mid = middle(numList)
        time.sleep(DELAY)
        print("\n")
        print("Middle: " + str(numList[mid]))
        time.sleep(0.5)
        selected = numList[mid]
        if selected != search and len(numList) == 1:
            if colour:
                shell.write("Number " + str(search) + " is not in list!\n","stderr")
            elif not colour:
                print("Number " + str(search) + " is not in list!")
            break

        elif selected > search:
            print(str(selected) + " is larger than " + str(search) + ". Removing upper half of the list.")
            time.sleep(DELAY)
            numList = numList[0:mid]
            print(numList)

        elif selected < search:
            print(str(selected) + " is smaller than " + str(search) + ". Removing lower half of the list.")
            time.sleep(DELAY)
            numList = numList[mid+1:]
            print(numList)

        elif selected == search:
            if colour:
                shell.write("Item Found!\n","STRING")
            elif not colour:
                print("Item Found!")
            pos = originalList.index(search) + 1
            suffix = "th"
            if pos == 1:
                suffix = "st"
            elif pos == 2:
                suffix = "nd"
            elif pos == 3:
                suffix = "rd"
            print("Was position " + str(originalList.index(search)) + "(" + str(pos) + suffix + " item) in original list!")
        
        if len(numList) == 0:
            if colour:
                shell.write("Number " + str(search) + " is not in list!\n","stderr")
            elif not colour:
                print("Number " + str(search) + " is not in list!")
            break
    
    again = "None"
    yesList = ["y","yes","yeah"]
    noList = ["n","no","nah"]

    while again.lower() not in yesList and again.lower() not in noList:
        again = input("\nRun again? [Y/N]:")
    if again.lower() in yesList:
        menu()
    elif again in noList:
        for i in range(0,100):
            print("\n")
        os._exit(0)


menu()
