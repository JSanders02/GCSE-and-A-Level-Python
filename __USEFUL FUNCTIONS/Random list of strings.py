import random

def randString(amount):
    strings = []
    for i in range(0,amount):
        string = []
        length = random.randint(1,10)
        print(str(length))
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
        

        

        
