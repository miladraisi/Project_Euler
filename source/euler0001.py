#!/usr/bin/python3

def main():
    number = 1000
    sum_of_number = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_number += i
    print(sum_of_number)

if __name__ == "__main__": main()
