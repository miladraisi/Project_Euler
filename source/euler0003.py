#!/usr/bin/python3

from eulerlib import is_prime

def main():
    '''main function'''
    number = 600851475143
    largest_prime = 0
    for i in range(1, int(number**0.5+1)):
        if is_prime(i) and number % i == 0:
            largest_prime = i
    print(largest_prime)

if __name__ == "__main__": main() 
