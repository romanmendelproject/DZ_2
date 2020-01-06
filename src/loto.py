import sys
from engine import Kegs, Players


if __name__ == '__main__':
    Keg = Kegs()
    player = Players('Человек')
    comp = Players('Компьютер')
    player.SetCard()
    comp.SetCard()
    print("\r")
    while True:
        num_keg = next(Keg.keg_gen)
        while True:
            player.GetCard(player.name, player.card_array)
            comp.GetCard(comp.name, comp.card_array)
            input_player = input('Зачеркнуть цифру? (y/n)')
            if input_player != 'n' and input_player != 'y':
                print('ВВЕДИТЕ y or n')
                continue
            elif input_player == 'y':
                if player.search(player.card_array, num_keg):
                    comp.search(comp.card_array, num_keg)
                    break
                else:
                    print('Вы проиграли')
                    sys.exit(1)
            elif input_player == 'n':
                if player.search(player.card_array, num_keg):
                    print('Вы проиграли')
                    sys.exit(1)
                elif comp.search(comp.card_array, num_keg):
                    break
            break
