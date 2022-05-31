#!/bin/python3

from codem import is_valid_v, mk_rand_codem, city_name


if __name__ == '__main__':
    quit = 0
    print(" (enter 1 to check and 2 to generate random melli code)")
    while(not quit):
        comm = input("> ")
        if(comm == '1'):
            print(is_valid_v(input("your code> ")))
        elif(comm == '2'):
            base = input("enter a base (city code) or leave it empty> ")
            if(len(base) > 8):
                break
            if(base == ''):
                base = None
            else:
                base = "0"*(3-len(base)) + base
                cn = city_name(base)
                if(cn is None):
                    print("%s is not a valid city code" % base)
                else:
                    print("محل صدور: %s" % cn)
            print(mk_rand_codem(base))
        elif(comm.replace(' ', '') == ''):
            pass
        else:
            quit = 1
