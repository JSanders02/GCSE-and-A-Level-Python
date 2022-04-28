from threading import Timer
global timeUp
timeUp = False
#Tells the program what to do when player runs out of time to guess
def outOfTime():
    global timeUp
    timeUp = True
    print("\nTime Up!")
t=Timer(5,outOfTime) #Timer(interval, function, arguments=[], keywordarguments={}) i.e. Timer(5, function, [arg1, arg2])
t.start() #Starts timer
answer = input('You have 5 seconds to type something: ')

if answer != None and not timeUp:
    print('Nice, you did it')
    t.cancel() #stops the timer
