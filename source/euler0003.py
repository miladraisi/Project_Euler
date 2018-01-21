#!/usr/bin/python3

def main():
    '''main function'''
    number = 600851475143
    largest_prime = 0
    for i in range(1, int(number**0.5+1)):
        if is_prime(i) and number % i == 0:
            largest_prime = i
    print(largest_prime)

def is_prime(num):
    '''if num is prime return true'''
    if num == 1:
        return False
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__": main() 
