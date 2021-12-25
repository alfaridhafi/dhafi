import utils
import random
    
print ('Memulai permainan batu gunting kertas')
player_name = input('masukkan nama anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')

player_hand = int(input('Masukkan nomor (0-2): '))
if utils.validate(player_hand):
    computer_hand = random.randint(0, 2)
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'komputer')

    result = utils.judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')