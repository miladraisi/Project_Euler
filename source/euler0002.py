#!/usr/bin/python3

from eulerlib import is_even

def main():
    '''main function'''
    a, b = 1, 2
    sumn = 0
    while a < 4000000:
        if is_even(a):
            sumn += a
        a, b = b, a + b
    print(sumn)

if __name__ == "__main__": main() 
