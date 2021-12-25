money = 30

fruits = {'apel': 3, 'jeruk': 4, 'semangka': 8}
for fruit in fruits:
    print('---------------------------------------------')
    print('anda memiliki uang sebanyak' + str(money) + 'dolar')
    print('harga setiap' + fruit + 'adalah' + str(fruits[fruit]) + 'dolar')

    variable_count = input('anda mau berapa' + fruit + '?')
    print('anda memilih' + variable_count)
    count = str(variable_count)
    total_price = fruits[fruit] * count
    print('total pembayaran anda adalah' + str(total_price) + 'dolar')
    if money >= total_price:
        print('anda telah membeli' + variable_count + '' + fruit)
        money -= total_price
        if money == 0:
            print('uang anda tidak cukup')
            break
    else:
        print('uang anda tidak cukup')
        print('anda tidak dapat membeli ' + fruit + 'sebanyak itu')
    print('uang anda tinggal ' + str(money) + 'dolar')
