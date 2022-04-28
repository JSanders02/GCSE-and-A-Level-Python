print('''


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@                            @@
@@                            @@
@@          1) Shrek          @@
@@                            @@
@@         2) Shrek 2         @@
@@                            @@
@@         3) Shrek 3         @@
@@                            @@
@@    4) Shrek 4ever after    @@
@@                            @@
@@    5) Shrek 5ever after    @@
@@                            @@
@@                            @@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

''')

choice = 'None'
choiceList =  ['1', '2', '3', '4', '5']

while choice not in choiceList:
    choice = input('Enter choice [1/2/3/4/5]: ') 
if choice == "1":
    time.sleep(0.5)
if choice == "2":
    time.sleep(0.5)
if choice == "3":
    time.sleep(0.5)
if choice == "4":
    time.sleep(0.5)
if choice == "5":
    time.sleep(0.5)
