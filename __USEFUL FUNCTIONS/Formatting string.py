def formatExample():
    #Using ':' prints words aligned to the left, '^' aligns to center, '>' aligns words to right
    print('{:10}: {:10} | {:10} | {:10} | {:5} | {:5} | {:10}'.format('{:[Int]}','Prints', 'Words', 'Aligned', 'To', 'The', 'Left'))
    print('\n')
    print('{:^10}: {:^10} | {:^10} | {:^10} | {:^5} | {:^5} | {:^10}'.format('{:^[Int]}','Prints', 'Words', 'Aligned', 'To', 'The', 'Center'))
    print('\n')
    print('{:>10}: {:>10} | {:>10} | {:>10} | {:>5} | {:>5} | {:>10}'.format('{:>[Int]}','Prints', 'Words', 'Aligned', 'To', 'The', 'Right'))
    print('\n\n')

def formatList(list):
    #For formatting lists, you need a * in front of the list name
    print('{:10}| {:10} | {:10} | {:10} | {:5} | {:5} | {:10}'.format(*list))

formatExample()
formatList(['{:[Int]}','Prints', 'Words', 'Aligned', 'To', 'The', 'Left'])