import random
import sys
from constants import row_card, column_card


class Card:
    def SetCard(self):
        """
        Формируем карточку игрока, разбивая по декадам рандобные числа,
        чтобы впоследствии разбить их по своим столбцам в карточке,
        также учитываем, что в последней декаде + число 90.
        """
        card_array = []
        start_decade = 0
        end_decade = 9
        penult_barrel = 89
        last_barrel = 90
#       формируем массив номеров в карточке
        for i in range(end_decade):
            card_array_item = []
            for j in range(row_card-1):
                while True:
                    if start_decade == 0:
                        start_decade += 1
                    card_item = random.randint(start_decade, end_decade)
                    if card_item not in card_array_item:
                        card_array_item.append(card_item)
                        break
                if j == 1:
                    card_array_item.append(" ")
            card_array.append(card_array_item)
            start_decade += 10
            end_decade += 10
            if end_decade == penult_barrel:  # учитываем 90 в последней декаде
                end_decade = last_barrel
#       после формирования массива остается 3 лишних числа, заменяем их рандомно.
        for i in range(row_card):
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
        """
        Выводим карточку на экран в читабельном виде
        username - имя пользователя(Компьютер или Человек)
        user_card - сформированный методом SetCard массив чисел 
        """
        print('{:#^35}'.format(" "+self.name+" "))
        for j in range(row_card):
            if j > 0:
                print(f"\r")
            for i in range(column_card):
                print(f"{user_card[i][j]:3}", end=" ")
        print(f"\n{'#'*35}")

    def search(self, user_card, num_keg):
        """
        Выполняем поиск выпавшего числа.
        user_card - сформированный методом SetCard массив чисел
        num_keg - выпавшее число
        """
        for j in range(column_card):
            for i in range(row_card):
                if user_card[j][i] == num_keg:
                    user_card[j][i] = "  X"
                    self.score += 1
                    print(f"Текущий счет {self.name}: {self.score}")
                    if self.score == 15:
                        print(f"Победил {self.name}")
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
