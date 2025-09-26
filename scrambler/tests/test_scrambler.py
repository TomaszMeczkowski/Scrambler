import pytest
from scrambler.views import scramble_word, scramble_text


def test_scramble_word_short_words():
    assert scramble_word("a") == "a"
    assert scramble_word("to") == "to"
    assert scramble_word("tak") == "tak"  # <=3 znaki, bez zmian


def test_scramble_word_long_word():
    word = "python"
    scrambled = scramble_word(word)
    # pierwszy i ostatni znak muszą być takie same
    assert scrambled[0] == "p"
    assert scrambled[-1] == "n"
    # długość nie może się zmienić
    assert len(scrambled) == len(word)
    # zawiera te same litery
    assert sorted(scrambled) == sorted(word)


def test_scramble_text_multiple_words():
    text = "Python Django"
    scrambled = scramble_text(text)
    assert len(scrambled.split()) == 2
