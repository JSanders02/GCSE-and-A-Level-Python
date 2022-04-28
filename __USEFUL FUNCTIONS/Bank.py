import time
def bank():
    def deposit():
        global cash
        global banked
        amount = 1000000000000000000000000000000000000000000000000000000
        while str(amount).isnumeric() == False or float(amount) > cash:
            amount = input("Enter amount to deposit IN POUNDS: ")

        amount = float(amount)    
        banked = banked + amount
        banked = float(banked)
        cash = cash - amount
        cash = float(cash)
        print("New balance: " + str(banked) + ".")
        time.sleep(0.5)
        print("New amount of cash: " + str(cash) + ".")
        
    def withdraw():
        global cash
        global banked
        amount = 1000000000000000000000000000000000000000000000000000000
        while str(amount).isnumeric() == False or float(amount) > banked:
            amount = input("Enter amount to withdraw IN POUNDS: ")

        amount = float(amount)    
        banked = banked - amount
        banked = float(banked)
        cash = cash + amount
        cash = float(cash)
        print("New balance: " + str(banked) + ".")
        time.sleep(0.5)
        print("New amount of cash: " + str(cash) + ".")

    depositList = ['d','deposit']
    withdrawList = ['w','withdraw']
    choice = None
    while choice != '0':
        DorW = input("Deposit or withdraw?: ")
        if DorW in depositList:
            deposit()
        if DorW in withdrawList:
            withdraw()

global cash
global banked
cash = float(100)
banked = float(0)

bank()
