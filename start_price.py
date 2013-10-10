def get_int(text):
    return int(input(u'%s' % text))

def get_start_price():
    price_one = get_int(u'Цена за постройку 1-го здания: ')
    price_two = get_int(u'Цена за постройку 2-х зданий: ')

    delta = price_two - price_one*2

    lvl = get_int(u'Текущий уровень: ')
    #now_price = get_int(u'Текущая цена: ')

    start_price = price_one - delta*lvl

    print('\t\tДельта %s' % delta)
    print('\t\tСтартовая цена %s' % start_price)

while True:
    try:
        get_start_price()
    except:
        break
