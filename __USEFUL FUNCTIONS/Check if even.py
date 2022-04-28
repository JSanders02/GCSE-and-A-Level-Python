def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

while True:
    n = int(input('Enter number to check if even: '))
    print(isEven(n))
