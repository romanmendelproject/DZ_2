import pytest
import random
from src.engine import Card
from src.constants import row_card, column_card


@pytest.fixture
def card():
    card = Card()
    card.SetCard()
    return card.card_array


@pytest.fixture
def card_num_int_range():
    return range(1, 91)
