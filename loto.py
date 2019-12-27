import random
import sys


class Card:
    def SetCard(self):
        card_array = []
        x, y = 0, 9
#       формируем массив номеров в карточке
        for i in range(9):
            card_array_item = []
            for j in range(2):
                while True:
                    if x == 0:
                        x += 1
                    card_item = random.randint(x, y)
                    if card_item not in card_array_item:
                        card_array_item.append(card_item)
                        break
                if j == 1:
                    card_array_item.append(" ")
            card_array.append(card_array_item)
            x += 10
            y += 10
            if y == 89:
                y += 1
#       удаляем лишние номера
        for i in range(3):
            while True:
                card_array_item = random.randint(0, 8)
                if isinstance(card_array[card_array_item][1], int):
                    card_array[card_array_item][1] = " "
                    break
#       раскидываем по 5 чисел в строке
        for i in range(4):
            while True:
                card_array_item = random.randint(0, 8)
                if isinstance(card_array[card_array_item][0], int):
                    card_array[card_array_item][2] = card_array[card_array_item][0]
                    card_array[card_array_item][0] = " "
                    break
        while True:
            card_array_item = random.randint(0, 8)
            if isinstance(card_array[card_array_item][1], int) and isinstance(card_array[card_array_item][2], str):
                card_array[card_array_item][2] = card_array[card_array_item][1]
                card_array[card_array_item][1] = " "
                break

        self.card_array = card_array

    def GetCard(self, username, user_card):
        print('{:#^35}'.format(" "+self.name+" "))
        for j in range(3):
            if j > 0:
                print(f"\r")
            for i in range(9):
                print(f"{user_card[i][j]:3}", end=" ")
        print(f"\n{'#'*35}")

    def search(self, user_card, num_keg):
        for j in range(9):
            for i in range(3):
                if user_card[j][i] == num_keg:
                    user_card[j][i] = "  X"
                    self.score += 1
                    print(f"Текущий счет {self.name}: {self.score}")
                    if self.score == 15:
                        print("Вы выиграли")
                        sys.exit(1)
                    return True
                else:
                    continue


class Players(Card):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score


class Kegs:
    def __init__(self):
        self.keg_gen = self.get_keg()

    def get_keg(self):
        lst = [x for x in range(1, 90)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('\n')
            print('Текущий бочонок: {} Осталось в мешке: {}\n'.format(y, 90 - (i+1)))
            yield y


if __name__ == '__main__':
    Keg = Kegs()
    player = Players('Человек')
    comp = Players('Компьютер')
    player.SetCard()
    comp.SetCard()
    print("\r")
    while True:
        num_keg = next(Keg.keg_gen)
        player.GetCard(player.name, player.card_array)
        comp.GetCard(comp.name, comp.card_array)
        input_player = input('Зачеркнуть цифру? (y/n)')
        if input_player == 'y':
            if player.search(player.card_array, num_keg):
                comp.search(comp.card_array, num_keg)
                continue
            else:
                print('Вы проиграли')
                sys.exit(1)
        if input_player == 'n':
            if player.search(player.card_array, num_keg):
                print('Вы проиграли')
                sys.exit(1)
            elif comp.search(comp.card_array, num_keg):
                continue
