def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount


price1 = -100
discount1 = 10
discounted(price1, discount1)


def get_summ(one, two, delimiter='&'):
    print(f'{one}{delimiter}{two}')


L = 'Learn'
P = 'Python'
get_summ(L, P)


def format_price(price):
    price = int(float(price))

    return f'Цена: {price} руб.'


price2 = input('Введи цену:')
intprice = format_price(price2)
print(intprice)
