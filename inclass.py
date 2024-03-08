# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:13:49 2024

@author: cjgri
"""

#1 factorial function 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  

#2
def print_fibonacci(n):
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n-1) + fib(n-2)
    for i in range(n):
        print(fib(i), end=' ')
    print()  

print_fibonacci(5)  
        
        
   


#3

def sierpinski(n, offset=0):
    if n == 0:
        print(' ' * offset + '^')
    else:
        sierpinski(n-1, offset + 2**(n-1))
        sierpinski(n-1, offset)
        sierpinski(n-1, offset + 2**n)

# Example usage
sierpinski(3)


