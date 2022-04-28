import os
import sys
import time
import random
import math as maths

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
            
    bucketSort(numList)

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
        numList.append(round(random.random(), 3))
        
    bucketSort(numList)

##Sort time fellas
def bucketSort(toSort):
    bucketList = [[],[],[],[],[],[],[],[],[],[]]
    for unsorted in toSort:
        bucketIndex = maths.trunc(10 * unsorted)
        bucket = bucketList[bucketIndex]
        if bucket == []:
            bucket.append(unsorted)
        else:
            insertIndex = -1
            for sortedItem in bucket:
                insertIndex += 1
                if sortedItem > unsorted:
                    bucket.insert(insertIndex, unsorted)
                    break
                elif insertIndex == len(bucket) - 1:
                    bucket.append(unsorted)
                    break
        bucketList[bucketIndex] = bucket
    print('Buckets:')
    for i in bucketList:
        print(i)
    
    print('\n')
    sortedList = []
    for i in bucketList:
        for e in i:
            sortedList.append(e)
    print(' | '.join([str(i) for i in sortedList]))
                
    if colour:
        shell.write("List has been sorted!\n","STRING")
    elif not colour:
        print("List has been sorted!")

menu()
