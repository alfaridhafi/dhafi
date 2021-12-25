from random import randint


def validate(hand):
    if hand < 0 or hand > 2:
        return False
        return True


def print_hand(hand, name):
    hands = ['Batu', 'Gunting', 'kertas']
    print(name + 'memilih' + hands[hand])


def judge(player, computer):
    if player == computer:
        return 'Seri'
    elif player == 0 and computer == 1:
        return 'Kalah'
    elif player == 1 and computer == 2:
        return 'Kalah'
    elif player == 2 and computer == 0:
        return'Kalah'
    else:
        return 'Menang'


print('Memulai permainan batu gunting kertas')
player_name = input('masukkan nama anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')

player_hand = int(input('Masukkan nomor (0-2): '))
if validate(player_hand):
    computer_hand = print_hand[randint(0, 2)]
    print_hand(player_hand, player_name)
    print_hand(computer_hand, 'guest')

    result = judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')
