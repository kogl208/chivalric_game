# -*- coding: utf-8 -*-
'''
@autor: Lev Bashaev
'''

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
    flag = 'y'

    name_build = raw_input('Enter name build(str): ')
    lvl_build = int_input('Enter lvl build(int): ')
    delta_build = int_input('Enter delta price build(int): ')
    now_price_build = int_input('Enter now price build(int): ')
    profit = int_input('Enter profit build(int): ')
    
    start_price = now_price_build - delta_build*lvl_build

    id = len(dict_build)
    dict_build[str(id)] = {'name': name_build, 'delta': delta_build, 'start_price': start_price, 
        'profit': profit}
    print('''Added building:
    Id: %s
    Name: %s
    Delta price: %s
    Start price: %s
    Profit: %s
    ''' % (id, name_build, delta_build, start_price, profit))
    
    flag = raw_input('Return(y/n)? ')
    if not flag.lower() in ('y', 'yes'):
        break
