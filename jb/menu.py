from menu_item import MenuItem

menu_item1 = MenuItem('roti bakar', 5)
menu_item2 = MenuItem('kopi', 4)
menu_item3 = MenuItem('jus jeruk', 6)
menu_item4 = MenuItem('kue lapis', 3)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4 ]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item,info() )
    index += 1 

print('--------------------')

order = int(input('Masukkan nomor menu: '))
selecter_menu = menu_items[order]
print('Item yang di pilih:' + selected_menu.name)

count = int(input('Jumlah pesanan (diskon 10% untuk 3 atau lebih): '))

result = selected_menu.get_total_price(count)

print('Total harga adalah $ ' + str(result))
