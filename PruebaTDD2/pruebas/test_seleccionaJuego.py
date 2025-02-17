import unittest
from wordle.ClaseWordle import ClaseWordle

def test_seleccionaJuego():
    wordle = ClaseWordle()
    wordle.seleccionaJuego()
    assert wordle.palabraJuego in ClaseWordle.palabras