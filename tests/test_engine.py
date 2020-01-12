import pytest
from src.engine import Card, Players, Kegs


def test_set_card_len_array_collumn(card):
    """Проверка количества столбцов карточки
    """
    assert len(card) == 9


def test_set_card_len_array_row(card):
    """Проверка количества строк карточки
    """
    for card_row in card:
        assert len(card_row) == 3


def test_set_card_number_sum(card):
    """Проверка общего количества чисел карточки
       и количество пустых клеток
    """
    number_count = 0
    null_count = 0
    for card_row in card:
        for card_collumn in card_row:
            if isinstance(card_collumn, int):
                number_count += 1
            elif card_collumn == " ":
                null_count += 1
    assert number_count == 15
    assert null_count == 12


def test_set_card_number_row_sum(card):
    """Проверка количества чисел в строке
    """
    number_count_row_1 = 0
    number_count_row_2 = 0
    number_count_row_3 = 0
    print(card)
    for card_row in card:
        if isinstance(card_row[0], int):
            number_count_row_1 += 1
        if isinstance(card_row[1], int):
            number_count_row_2 += 1
        if isinstance(card_row[2], int):
            number_count_row_3 += 1
    assert number_count_row_1 == 5
    assert number_count_row_2 == 5
    assert number_count_row_3 == 5


def test_set_card_number_col_sum(card):
    """Проверка количества чисел в столбце
    """
    for card_row in card:
        card_collumn_sum = 0
        for card_collumn in card_row:
            if isinstance(card_collumn, int):
                card_collumn_sum += 1
        assert card_collumn_sum in [1, 2]


def test_set_card_number_range(card, card_num_int_range):
    """Проверка попадания чисел карточки в диапазон [1-90]
    """
    for card_row in card:
        for card_collumn in card_row:
            if isinstance(card_collumn, int):
                assert card_collumn in card_num_int_range


def test_search_score(card):
    """Проверка счета при победе.
    """
    card_search = Players("test")
    lst = [x for x in range(1, 91)]
    try:
        for keg in lst:
            card_search.search(card, keg)
    except SystemExit:
        assert card_search.score == 15
        assert card_search.name == "test"


def test_search_remove_keg(card):
    """Проверка удаления выпавшего числа.
    """
    card_search = Players("test")
    lst = [x for x in range(1, 91)]
    try:
        for keg in lst:
            card_search.search(card, keg)
            if card_search.score == 1:
                for card_row in card:
                    assert keg not in card_row
    except SystemExit:
        pass


def test_search_replace_keg(card):
    """Проверка замены всех выпавших чисел.
    """
    card_search = Players("test")
    lst = [x for x in range(1, 91)]
    try:
        for keg in lst:
            card_search.search(card, keg)
    except SystemExit:
        countX = 0
        for card_row in card:
            countX += card_row.count("  X")
        assert countX == 15


def test_get_keg_sum():
    """Проверка общего количества боченков.
    """
    keg = Kegs()
    CountGen = 0
    while True:
        try:
            next(keg.keg_gen)
            CountGen += 1
        except StopIteration:
            assert CountGen == 90
            break


def test_get_keg_range(card_num_int_range):
    """Проверка попадания чисел в мешке в диапазон [1-90]
    """
    keg = Kegs()
    while True:
        try:
            assert next(keg.keg_gen) in card_num_int_range
        except StopIteration:
            break