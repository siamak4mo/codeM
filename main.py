#!/bin/python3

from codem import is_valid_v, mk_rand_codem


if __name__ == '__main__':
    quit = 0
    print("1 to check and 2 to gen")
    while(not quit):
        comm = input("> ")
        if(comm == '1'):
            print(is_valid_v(input("your code> ")))
        elif(comm == '2'):
            print(mk_rand_codem())
        else:
            quit = 1
