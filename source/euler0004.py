#!/usr/bin/python3

from eulerlib import reverse

def main():
    '''main function'''
    temp = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            temp1 = i * j
            if temp1 > temp and temp1 == reverse(temp1):
                temp = temp1
    print(temp)

if __name__ == "__main__": main()
