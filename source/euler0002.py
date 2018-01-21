#!/usr/bin/python3

def main():
    '''main function'''
    a, b = 1, 2
    sumn = 0
    while a < 4000000:
        if is_even(a):
            sumn += a
        a, b = b, a + b
    print(sumn)

def is_even(num):
    '''if num is even return true'''
    if num % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__": main() 
