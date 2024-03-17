#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    
    while countdown > 0:
        print(countdown)
        countdown -= 1

    print('Happy New Year!')


def square_integers(int_list):
    out_list = []
    
    for num in int_list:
        out_list.append(num*num)

    return out_list    

def fizzbuzz():
    for num in range(100):
        real_num = num + 1
        
        if (real_num % 3 == 0) & (real_num % 5 == 0):
            print('FizzBuzz')
        elif (real_num % 3 == 0):
            print('Fizz')
        elif (real_num % 5 == 0):
            print('Buzz')
        else:
            print(real_num)
