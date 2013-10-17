# -*- coding: utf-8 -*-
'''
@author: Lev Bashaev
@note: Find max profit, max defense-point or attack-point
'''
from copy import copy


'''
profit == profit
'''
builds_money = {'0': {'name': "Попрошайка", 'lvl': 0, 'delta': 1050, 'profit': 100, 'start_price': 10500},
                '1': {'name': "Крестьянин", 'lvl': 0, 'delta': 12000, 'profit': 1000, 'start_price': 120000},
                '2': {'name': "Шут",'lvl': 0, 'delta': 67500, 'profit': 5000, 'start_price': 675000},
                '3': {'name': "Палач", 'lvl': 0, 'delta': 375000, 'profit': 25000, 'start_price': 3750000},
                '4': {'name': "Бродячий монах", 'lvl': 0, 'delta': 2400000, 'profit': 100000, 'start_price': 24000000},
                '5': {'name': "Алхимик", 'lvl': 0, 'delta': 6750000, 'profit': 250000, 'start_price': 67500000},
                '6': {'name': "Сквайр", 'lvl': 0, 'delta': 11250000, 'profit': 375000, 'start_price': 112500000},
                '7': {'name': "Торговец", 'lvl': 0, 'delta': 20250000, 'profit': 450000, 'start_price': 202500000},
                '8': {'name': "Рыцарь", 'lvl': 0, 'delta': 30600000, 'profit': 600000, 'start_price': 306000000},
                }


'''
profit == attack
'''
builds_att ={'0': {'name': "Попрошайка", 'lvl': 0, 'delta': 1050, 'profit': 3, 'start_price': 10500},
                '1': {'name': "Крестьянин", 'lvl': 0, 'delta': 12000, 'profit': 6, 'start_price': 120000},
                '2': {'name': "Шут",'lvl': 0, 'delta': 67500, 'profit': 9, 'start_price': 675000},
                '3': {'name': "Палач", 'lvl': 0, 'delta': 375000, 'profit': 16, 'start_price': 3750000},
                '4': {'name': "Бродячий монах", 'lvl': 0, 'delta': 2400000, 'profit': 25, 'start_price': 24000000},
                '5': {'name': "Алхимик", 'lvl': 0, 'delta': 6750000, 'profit': 45, 'start_price': 67500000},
                '6': {'name': "Сквайр", 'lvl': 0, 'delta': 11250000, 'profit': 60, 'start_price': 112500000},
                '7': {'name': "Торговец", 'lvl': 0, 'delta': 20250000, 'profit': 1, 'start_price': 202500000},
                '8': {'name': "Рыцарь", 'lvl': 0, 'delta': 30600000, 'profit': 175, 'start_price': 306000000},
                }


'''
profit == defense
'''
builds_def ={'0': {'name': "Попрошайка", 'lvl': 0, 'delta': 1050, 'profit': 3, 'start_price': 10500},
                '1': {'name': "Крестьянин", 'lvl': 0, 'delta': 12000, 'profit': 4, 'start_price': 120000},
                '2': {'name': "Шут",'lvl': 0, 'delta': 67500, 'profit': 11, 'start_price': 675000},
                '3': {'name': "Палач", 'lvl': 0, 'delta': 375000, 'profit': 14, 'start_price': 3750000},
                '4': {'name': "Бродячий монах", 'lvl': 0, 'delta': 2400000, 'profit': 25, 'start_price': 24000000},
                '5': {'name': "Алхимик", 'lvl': 0, 'delta': 6750000, 'profit': 42, 'start_price': 67500000},
                '6': {'name': "Сквайр", 'lvl': 0, 'delta': 11250000, 'profit': 6, 'start_price': 112500000},
                '7': {'name': "Торговец", 'lvl': 0, 'delta': 20250000, 'profit': 110, 'start_price': 202500000},
                '8': {'name': "Рыцарь", 'lvl': 0, 'delta': 30600000, 'profit': 180, 'start_price': 306000000},
                }


def main():
    builds, TEXT = get_choise()
    money = get_money()
    
    builds_copy = get_lvl_builds(copy(builds))
            
    summ = {}
    for key, build in builds_copy.items():
        summ.setdefault(key, {'name': build['name'], 'price': 0, 'profit': 0, 'delta_lvl': 0})
    
    summ = finde_max_profit(money, builds_copy, summ)
    print_end_text(summ, TEXT, money)


def finde_max_profit(money, builds, summ):
    price_all_builds = 0
    money_now = copy(money)
    while True:
        price_build = get_price_buld_now(builds)
        sorted_max_in_up(price_build)
        while True:
            if len(price_build) > 0:
                perfect_build = price_build[0]
                if perfect_build[2] > money_now:
                    price_build.pop(0)
                else:
                    break
            else:
                break
                
        cash_for_test = perfect_build[2]
        profit_for_test = perfect_build[1]
        
        temp_summ = {}
        temp_data = []
        
        for key, build in builds.items():
            temp_summ.setdefault(key, {'name': '', 'price': 0})
            price = 0
            start_lvl = build['lvl']
            delta_lvl = 0
            start_price = get_build_price(**build)
            build_copy = copy(build)
            while price + temp_summ[key]['price'] + build_copy['delta'] < cash_for_test:
                if start_price['price'] > cash_for_test: break
                temp_summ[key] = get_build_price(**build_copy)
                delta_lvl += 1
                build_copy['lvl'] += 1
                price += temp_summ[key]['price']
            profit = delta_lvl * build_copy['profit']
            temp_data.append((build_copy['name'], price, profit, delta_lvl, key))
        sorted_max_in_up(temp_data)
        max_profit_build = temp_data[0]

        if price_all_builds + max_profit_build[1] > money:
            break
        key = max_profit_build[4]
        summ[key]['profit'] += max_profit_build[2]
        summ[key]['price'] += max_profit_build[1]
        summ[key]['delta_lvl'] += int(max_profit_build[3])
        builds[key]['lvl'] += int(max_profit_build[3])
        price_all_builds += max_profit_build[1]
        money_now -= max_profit_build[1]
    return summ


def get_lvl_builds(builds):
    print("Введите уровень:")
    for line in range(len(builds)):
        try:
            while True:
                try:
                    builds[str(line)]['lvl'] = int(input('\t"{0}": '.format(
                                                        builds[str(line)]['name'])))
                    break
                except NameError:
                    pass
        except (SyntaxError, ValueError):
            builds[str(line)]['lvl'] = 1 << 100
    return builds


def get_money():
    try:
        money = int(input("Введите количесство денег: "))
    except (NameError, ValueError, SyntaxError):
        money = 0
    return money


def set_len(text, len_str=None):
    if not len_str or len_str<len(text):
        return text
    else:
        add_text = ''*(len_str - len(text))
    return text + add_text


def print_end_text(summ, TEXT, money):
    end_data = []
    for build in summ.values():
        if build['delta_lvl'] != 0:
            end_data.append((build['name'], build['price'], build['profit'], build['delta_lvl']))
    print('\n\n{0:20}{1:>20}'.format('Всего денег:', num_for_print(money)))
    end_price = sum_in_list(end_data, 1)
    end_profit = sum_in_list(end_data, 2)
    print('{0:20}{1:>20}'.format('Общая стоимость:', num_for_print(end_price)))
    print('-' * 40)
    print('{0:20}{1:>20}'.format('Остаток:', num_for_print(int(money) - end_price)))
    print('\n{0:20}{1:>20}'.format(TEXT, num_for_print(end_profit)))
    try:
        print_builds(len(end_data), end_data, TEXT)
    except IndexError:
        print('Не хавтает денег, что бы хоть что-то посторойть.')


def get_choise():
    try:
        flag = int(input('1 - на деньги\n2 - на защиту\nЛюбая другая цифра(символ) - на атаку\n'))
    except (NameError, ValueError, SyntaxError):
        flag = 3
        
    if flag == 1:
        print('...Наибольшая ПРИБЫЛЬ...')
        TEXT = 'Прибыль'
        return builds_money, TEXT
    elif flag == 2:
        TEXT = 'Защита'
        print('...Лучшая ЗАЩИТА...')
        return builds_def, TEXT
    else:
        TEXT = 'Атака'
        print('...Лучшая АТАКА...')
        return builds_att, TEXT

def sum_in_list(data, pos):
    end_sum = 0
    for build in data:
        end_sum += int(build[pos])
    return end_sum


def print_builds(len_builds, data, TEXT):
    sorted_max_in_up(data)
    print('\n\n{0:^30}{1:^20}{2:^20}{3:^15}'.format('Название', "Цена", TEXT, "Уровень"))
    print('='*85)
    for i in range(len_builds):
        print('{0:30}{1:20}{2:20}{3:15}'.format(data[i][0], num_for_print(data[i][1]), num_for_print(data[i][2]), num_for_print(data[i][3])))
        print('_'*75)


def sorted_max_in_up(data, key=None):
    if not key:
        data.sort(key=for_key)
        if data[0][2] != max(data, key=for_key):
            data.sort(key=for_key, reverse=True)
    else:
        data.sort(key=key)
        if data[0][2] != max(data, key=key):
            data.sort(key=key, reverse=True)


def for_key(data):
    return data[2], data[1]
    
      
def get_price_buld_now(builds):
    price = []
    price_now = []
    for build in builds.values():
        price.append(get_build_price(**build))
    for price_build in price:
        price_now.append((price_build['name'], price_build['profit'], price_build['price']))
    sorted_max_in_up(price_now)
    return price_now


def get_build_price(lvl, delta, profit, start_price, name):
    price = lvl * delta + start_price
    return {'profit': profit, 'name': name, 'price': price}


def num_for_print(num):
    str_num = str(num)
    rev_str_num = "".join(reversed(str_num))
    end_str_num = ""
    for line, char in enumerate(rev_str_num):
        end_str_num += char
        if (line + 1) % 3 == 0:
            end_str_num += ","
    end_str_num = end_str_num.rstrip(",")
    return "".join(reversed(end_str_num))


main()
input('Press Enter to exit...')
