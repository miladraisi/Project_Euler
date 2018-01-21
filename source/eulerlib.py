def is_even(num):
    '''if num is even return true'''
    if num % 2 == 0:
        return True
    else:
        return False

def is_prime(num):
    '''if num is prime return true'''
    if num <= 1:
        return False
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True

def reverse(num):
    '''return the reverse of num'''
    sumn = 0
    while num > 0:
        sumn = sumn * 10 + num % 10
        num //= 10
    return sumn
