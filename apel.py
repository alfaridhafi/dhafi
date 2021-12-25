money = 20

fruits = {'jeruk': 3, 'apel': 4, 'pisang': 5}
for fruit in fruits:
    print('--------------------------------------------------')
    print('anda memiliki uang sebanyak' + str(money) + 'dolar')
    print('harga setiap' + fruit + 'adalah' + str(fruits[fruit]) + 'dolar')

    input_count = input('mau berapa' + fruit + '?')
    print('anda akan membeli' + input_count)
    count = str(input_count)
    total_price = fruits[fruit] * count
    print('total pembayaran anda adalah' + str(total_price) + 'dolar')
    if money >= total_price:
        print('Anda telah membeli' + input_count + '' + fruit)
        money -= total_price
        if money == 0:
            print('uang anda tidak cukup')
            break
    else:
        print('Uang Anda tidak mencukupi')
        print('Anda tidak dapat membel' + fruit +  'sebanyak itu')
    print('uang anda tinggal' + str(money) + 'dolar')