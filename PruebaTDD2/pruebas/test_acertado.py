import unittest
from wordle.ClaseWordle import ClaseWordle

def test_acertado():
    wordle = ClaseWordle()
    wordle.palabraJuego = "PLAYA"
    intento = "PALYA"
    assert wordle.acertado == True