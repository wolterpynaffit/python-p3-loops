#!/usr/bin/env python3

def happy_new_year():
    i = 11
    while i >= 0:
        i -= 1
        print(i)
        if i == 1:
            print('Happy New Year!')
            break


def square_integers(int_list):
    squared = [i ** 2 for i in int_list]
    return squared


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
    # i = 101
    # while i >= 0:
    #     if i % 3 == 0 and i % 5 == 0:
    #         if i == 0:
    #             print('FizzBuzz')
    #     elif i % 3 == 0:
    #         print('Fizz')
    #     elif i % 5 == 0:
    #         print('Buzz')
    #     else:
    #         print(i)
    #     i -= 1


fizzbuzz()
