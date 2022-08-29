def cafe(array):
    price = 0
    dinner_price = []
    coupon = []
    i = 0
    indexes = []
    while len(array) > 0:
        i += 1
        cur_price = array.pop()
        if len(dinner_price) < len(coupon):
            dinner_price.append(cur_price)
            indexes.append(i)
        else:
            if len(coupon) == 0:
                if cur_price > 100:
                    coupon.append(cur_price)
                else:
                    price += cur_price
                continue

            if cur_price < dinner_price[-1]:
                if cur_price > 100:
                    coupon.append(cur_price)
                else:
                    price += cur_price

            else:
                last_bought = dinner_price.pop()
                indexes.pop()
                dinner_price.append(cur_price)
                indexes.append(i)
                if last_bought > 100:
                    coupon.append(last_bought)
                else:
                    price += last_bought

    print(price + sum(coupon))
    print(len(coupon) - len(dinner_price), len(dinner_price))
    for i in indexes:
        print(i)


data = [110, 110, 110]
data2 = [110, 40, 110, 120, 60, 110, 120]
cafe(data[::-1])
cafe(data2[::-1])
