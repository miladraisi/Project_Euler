#!/usr/bin/python3

import fractions

def main():
    '''main function'''
    ans = 1
    for i in range(1,21):
        ans *= i // fractions.gcd(i, ans)
    print(ans)

if __name__ == "__main__": main()
