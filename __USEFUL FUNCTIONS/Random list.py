import random
import sys

try:
    shell = sys.stdout.shell
    colour = True
except AttributeError:
    print("You must run this program in IDLE for colours. Program will run in colourless mode.")
    colour = False

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
    print(numList)

listGenerator()
    
