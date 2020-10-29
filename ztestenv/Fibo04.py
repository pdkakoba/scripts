#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Personal
#
# Created:     18/05/2014
# Copyright:   (c) Personal 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
def main():
    pass

if __name__ == '__main__':
    main()
"""
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b),
        a, b = b, a+b
    return a, b

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

x=fib(9)
print (x)
