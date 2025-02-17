import unittest
from parchis.Parchis import Parchis

def test_EsGanador():
    parchis = Parchis("Juan", "Pepe")
    parchis.fichaJ1 = Parchis.TAM_TABLERO
    assert parchis.esGanador() == "Juan"

def test_EsGanador2():
    parchis = Parchis("Juan", "Pepe")
    parchis.fichaJ2 = Parchis.TAM_TABLERO
    assert parchis.esGanador() == "Pepe"

def test_EsGanador():
    parchis = Parchis("Juan", "Pepe")
    parchis.fichaJ1 = 7
    parchis.fichaJ2 = 8
    assert parchis.esGanador() == ""
