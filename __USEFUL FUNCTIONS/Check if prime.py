def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

while True:
    n = int(input('Enter number to check if prime: '))
    print(isPrime(n))