import unittest
from wordle.ClaseWordle import ClaseWordle

def test_realizaIntento():
    wordle = ClaseWordle()
    intento = "LAMAS"
    wordle.realizaIntento(intento)
    assert wordle.pistas[0][0] == intento

def test_realizaIntento2():
    wordle = ClaseWordle()
    wordle.palabraJuego = "PLAYA"
    intento = "PLATO"
    wordle.realizaIntento(intento)
    assert wordle.pistas[0][1] == "PLA--"

def test_realizaIntento3():
    wordle = ClaseWordle()
    wordle.palabraJuego = "PLAYA"
    intento = "PALOS"
    wordle.realizaIntento(intento)
    assert wordle.pistas[0][1] == "P**--"
