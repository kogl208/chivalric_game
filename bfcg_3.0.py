# -*- coding: utf-8 -*-
'''
@author: Lev Bashaev
@note: Find max profit, max defense-point or max attack-point
'''
from copy import copy, deepcopy

BUILDINGS = {'0': {'name': "Попрошайка", 'lvl': 0, 'delta': 1050,
                   'profit': 100, 'attack': 3, 'defense': 3, 'start_price': 10500},
             '1': {'name': "Крестьянин", 'lvl': 0, 'delta': 12000,
                   'profit': 1000, 'attack': 6, 'defense': 4, 'start_price': 120000},
             '2': {'name': "Шут",'lvl': 0,'delta': 67500,
                   'profit': 5000, 'attack': 9, 'defense': 11, 'start_price': 675000},
             '3': {'name': "Палач", 'lvl': 0, 'delta': 375000,
                   'profit': 25000, 'attack': 16, 'defense': 14, 'start_price': 3750000},
             '4': {'name': "Бродячий монах", 'lvl': 0, 'delta': 2400000,
                   'profit': 100000, 'attack': 25, 'defense': 25, 'start_price': 24000000},
             '5': {'name': "Алхимик", 'lvl': 0, 'delta': 6750000,
                   'profit': 250000, 'attack': 45, 'defense': 42, 'start_price': 67500000},
             '6': {'name': "Сквайр", 'lvl': 0, 'delta': 11250000,
                   'profit': 375000, 'attack': 60, 'defense': 66, 'start_price': 112500000},
             '7': {'name': "Торговец", 'lvl': 0, 'delta': 20250000,
                   'profit': 450000, 'attack': 120, 'defense': 110, 'start_price': 202500000},
             '8': {'name': "Рыцарь", 'lvl': 0, 'delta': 30600000,
                   'profit': 600000, 'attack': 175, 'defense': 180, 'start_price': 306000000},
             '9': {'name': "Епископ", 'lvl': 0, 'delta': 54000000,
                   'profit': 900000, 'attack': 220, 'defense': 235, 'start_price': 540000000},
             '10': {'name': "Лорд", 'lvl': 0, 'delta': 99000000,
                   'profit': 1500000, 'attack': 320, 'defense': 310, 'start_price': 990000000},
             }
def main():
    money = get_money()
    choise, TEXT, percent = get_choise()
    get_lvl_builds(BUILDINGS)
    end_buildings = finde_max_profit(BUILDINGS, money, choise, percent)
    print_end_text(end_buildings, TEXT, money, choise, BUILDINGS, percent)
    
def finde_max_profit(BUILDINGS, money, choise, percent):
    price_all_bildings = 0
    money_now = copy(money)
    end_buildings = {}
    for key in BUILDINGS.keys():
        end_buildings.setdefault(key, 0)

    copy_buildings = []
    for key, value in BUILDINGS.items():
        profit = choise
        copy_buildings.append(Building(key, value['lvl'], value['delta'], value['start_price'], value[profit], percent))
    copy_buildings.sort(key=lambda l: int(l.key))

    jp = 0
    while True:
        buildings = deepcopy(copy_buildings)
        del_flag = len(buildings)
        for building in buildings:
            if building.price > money_now:
                building.lvl = 1 << 100
                del_flag -= 1
       
        if del_flag == 0:
            break
        max_profit = max(buildings, key=lambda l: l.del_profit)
        end_buildings[max_profit.key] += 1
        money_now -= max_profit.price
        copy_buildings[int(max_profit.key)].lvl += 1
        del buildings
    return end_buildings

        
class Building(object):
    def __init__(self, key, lvl, delta, start_price, profit, percent):
        self.key = key
        self.delta = delta
        self.start_price = start_price
        self.lvl = lvl
        self.profit = int(profit * (1 + percent/100))

    @property
    def price(self):
        return self.lvl * self.delta + self.start_price

    @property
    def del_profit(self):
        return self.profit / self.price

    
def get_lvl_builds(BUILDINGS):
    print("Введите уровень:")
    for line in range(len(BUILDINGS)):
        try:
            while True:
                try:
                    BUILDINGS[str(line)]['lvl'] = int(input('\t"{0}": '.format(
                                                        BUILDINGS[str(line)]['name'])))
                    break
                except NameError:
                    pass
        except (SyntaxError, ValueError):
            BUILDINGS[str(line)]['lvl'] = 1 << 100


def get_money():
    try:
        money = int(input("Введите количесство денег: "))
    except (NameError, ValueError, SyntaxError):
        money = 0
    return money


def print_end_text(end_buildings, TEXT, money, choise, BUILDINGS, percent):
    end_data = []
    buildings = []
    for key, value in BUILDINGS.items():
        buildings.append(Building(key, value['lvl'], value['delta'], value['start_price'], value[choise], percent))
    buildings.sort(key=lambda l: int(l.key))
        
    for key, building in BUILDINGS.items():
        if end_buildings[key] != 0:
            price = 0
            for iteration in range(end_buildings[key]):
                price += buildings[int(key)].price
                buildings[int(key)].lvl += 1
            profit = end_buildings[key] * buildings[int(key)].profit
            end_data.append((BUILDINGS[key]['name'], price, profit, end_buildings[key]))
        
    print('\n\n{0:20}{1:>20}'.format('Всего денег:', num_for_print(money)))
    end_price = sum_in_list(end_data, 1)
    end_profit = sum_in_list(end_data, 2)
    print('{0:20}{1:>20}'.format('Общая стоимость:', num_for_print(end_price)))
    print('-' * 40)
    print('{0:20}{1:>20}'.format('Остаток:', num_for_print(int(money) - end_price)))
    print('\n{0:20}{1:>20}'.format(TEXT, num_for_print(end_profit)))
    try:
        print_buildings(len(end_data), end_data, TEXT)
    except IndexError:
        print('Не хавтает денег, что бы хоть что-то посторойть.')


def print_buildings(len_buildings, data, TEXT):
    sorted_max_in_up(data)
    print('\n\n{0:^20}{1:^20}{2:^20}{3:^10}'.format('Название', "Цена", TEXT, "Уровень"))
    print('='*70)
    for i in range(len_buildings):
        print('{0:20}{1:20}{2:20}{3:10}'.format(data[i][0], num_for_print(data[i][1]), num_for_print(data[i][2]), num_for_print(data[i][3])))
        print('_'*70)


def get_choise():
    try:
        flag = int(input('1 - на деньги\n2 - на защиту\nЛюбая другая цифра(символ) - на атаку:\t'))
    except (NameError, ValueError, SyntaxError):
        flag = 3

    if flag == 1:
        try:
            percent = int(input('Введите дополнительный процент прибыли: '))
        except (NameError, ValueError, SyntaxError):
            percent = 0
        print('...Наибольшая ПРИБЫЛЬ...')
        TEXT = 'Прибыль'
        return 'profit', TEXT, percent
    elif flag == 2:
        TEXT = 'Защита'
        print('...Лучшая ЗАЩИТА...')
        return 'defense', TEXT, 0
    else:
        TEXT = 'Атака'
        print('...Лучшая АТАКА...')
        return 'attack', TEXT, 0


def sum_in_list(data, pos):
    end_sum = 0
    for build in data:
        end_sum += int(build[pos])
    return end_sum


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
input()
