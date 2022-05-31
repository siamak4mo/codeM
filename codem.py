import random
from valid_city_codes import valid_codes, valid_names


def find_nameH(code):
    for i in range(len(valid_codes)):
        if(valid_codes[i].count(str(code)) != 0):
            return i
    return -1


def find_name(code):
    i = find_nameH(code)
    if(i == -1):
        return None
    else:
        return valid_names[i]


def is_validH(codem):
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
#   return city name of codem
#   if not exist return None
def city_name(codem):
    city_name2 = find_name(codem[0:2])
    city_name3 = find_name(codem[0:3])
    if(city_name2 is None and city_name3 is None):
        return None
    else:
        return(city_name2 if city_name3 is None else city_name3)


#
# codem: @String of melli (meili) code
#        if len(codem) > 10 then return False
#        if len(codem) < 8  then will append enough 0 at the start
# output is an array (len=2)
# is_valid(*)[0]: validation result,  is_valid(*)[1]: city name
def is_valid(codem):
    if(len(codem) > 10 or len(codem) < 7):
        return([False, None])
    codem = "0"*(10-len(codem)) + codem
    last_c = is_validH(codem)
    if(last_c == int(codem[9])):
        return([True, city_name(codem)])
    else:
        return([False, None])


#
# verbos version of is_valid
# output is a string message
def is_valid_v(codem):
    if(len(codem) > 10 or len(codem) < 7):
        return "length of your input is not valid"
    codem = "0"*(10-len(codem)) + codem
    last_c = is_validH(codem)
    if(last_c == int(codem[9])):
        mess = "this code is Valid,\n"
        cn = city_name(codem)
        if(cn is None):
            mess += "but city code is not valid or is not in this archive\n"
            mess += "if you are sure about correctness of your melli code\n"
            mess += "please make a pull request on our github page."
        else:
            mess += "محل صدور: "
            mess += cn
        return mess
    else:
        return("** Not Valid, \n" +
               "the last charecter must be %d" % last_c)


#
# make a random melli code
# base will be at the beginning of output
def mk_rand_codem(base=None):
    if(base is None):
        codem = random.choice(random.choice(valid_codes))
    else:
        codem = base
    for _ in range((9-len(codem))):
        codem += str(random.randint(0, 9))
    codem += str(is_validH(codem + '0'))
    return codem
