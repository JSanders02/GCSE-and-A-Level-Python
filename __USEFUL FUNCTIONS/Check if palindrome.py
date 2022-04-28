def ifPalindrome(x):
    newX = [i for i in x]
    newX.reverse()
    newX = ''.join(newX)
    print(newX)
    if newX.lower() == x.lower():
        return True
    else:
        return False

while True:
    word = input('Enter word to check if palindrome: ')
    print(ifPalindrome(word))
