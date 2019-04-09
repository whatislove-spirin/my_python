def calculateUsingStack(expr):
    '''
    >>> calculateUsingStack("1 2 + 4 * 3 +")
    '15'
    >>> calculateUsingStack("1 2 3 * + 2 -")
    '5'
    '''
    stack = []
    for i in expr:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            first = stack.pop()
            second = stack.pop()
            stack.append(int(first)+int(second))
        elif i == '-':
            first = stack.pop()
            second = stack.pop()
            stack.append(int(second)-int(first))
        elif i == '*':
            first = stack.pop()
            second = stack.pop()
            stack.append(int(second)*int(first)) 
    return str(stack[0])

print(calculateUsingStack("1 2 3 * + 2 -"))
print(calculateUsingStack("1 2 + 4 * 3 +"))

import doctest
doctest.testmod()
