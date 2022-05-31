import random
from valid_city_codes import find_name, get_random


def is_validH(codem):
    # codem is a string and len(codem) must be 10
    # this is a helper function, dont use it
    ws = 0
    for i in range(8, -1, -1):
        ws += (10-i)*int(codem[i])
    R = ws % 11
    conn = R
    if(R >= 2):
        conn = 11 - conn
    return conn


#
# codem: @String of melli (meili) code
#        if len(codem) > 10 then return False
#        if len(codem) < 8  then will append enough 0 at the start
def is_valid(codem):
    if(len(codem) > 10 or len(codem) < 7):
        return "length of your input is not valid"
    codem = "0"*(10-len(codem)) + codem
    last_c = is_validH(codem)
    if(last_c == int(codem[9])):
        mess = "this code is Valid,\n"
        city_name2 = find_name(codem[0:2])
        city_name3 = find_name(codem[0:3])
        if(city_name2 is None and city_name3 is None):
            mess += "but city code is not valid or is not in this archive\n"
            mess += "if you are sure about correctness of your melli code\n"
            mess += "please make a pull request on our github page."
        else:
            mess += "محل صدور: "
            mess += city_name2 if city_name3 is None else city_name3
        return mess
    else:
        return("** Not Valid, \n" +
               "the last charecter must be %d" % last_c)


#
# make a random melli code
def mk_rand_codem():
    codem = get_random()
    for _ in range((9-len(codem))):
        codem += str(random.randint(0, 9))
    codem += str(is_validH(codem + '0'))
    return codem
