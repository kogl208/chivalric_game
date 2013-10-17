# -*- coding: utf-8 -*-
'''
@autor: Lev Bashaev
'''

def raw_input(text):
    return input(text)


def int_input(text):
    while True:
        try:
            number = int(raw_input(text))
            break
        except ValueError:
            pass
    return number


dict_build = {}


while True:

    name_build = raw_input('Enter name build(str): ')
    lvl_build = int_input('Enter lvl build(int): ')
    delta_build = int_input('Enter delta price build(int): ')
    now_price_build = int_input('Enter now price build(int): ')
    profit = int_input('Enter profit build(int): ')
    
    start_price = now_price_build - delta_build*lvl_build

    id = len(dict_build)
    dict_build[id] = {'name': name_build, 'lvl': 0, 'delta': delta_build, 'profit': profit,
                      'start_price': start_price}
    print('''Added building:
    Id: %s
    Name: %s
    Delta price: %s
    Start price: %s
    Profit: %s
    ''' % (id, name_build, delta_build, start_price, profit))
    
    flag = raw_input('Return(y/n)? ')
    if flag.lower() in ('n', 'no'):
        f = open('dict_build.txt', 'a')
        f.write('\n')
        f.write(str(dict_build))
        f.close()
        break
