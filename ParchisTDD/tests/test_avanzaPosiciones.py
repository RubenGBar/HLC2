import unittest
from parchis.Parchis import Parchis

def test_avanzaPosiciones():
    parchis = Parchis("Juan", "Pepe")
    Parchis.dado1 = 5
    Parchis.dado2 = 2
    res = 7
    parchis.fichaJ1 = 3
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == 10

def test_avanzaPosiciones2():
    parchis = Parchis("Juan", "Pepe")
    Parchis.dado1 = 5
    Parchis.dado2 = 3
    res = 8
    parchis.fichaJ2 = 5
    parchis.avanzaPosiciones(2)
    assert parchis.fichaJ2 == 13

def test_avanzaPosiciones3():
    parchis = Parchis("Juan", "Pepe")
    Parchis.dado1 = 5
    Parchis.dado2 = 3
    res = 8
    parchis.fichaJ1 = 13
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == 19

def test_avanzaPosiciones4():
    parchis = Parchis("Juan", "Pepe")
    Parchis.dado1 = 3
    Parchis.dado2 = 2
    res = 5
    parchis.fichaJ2 = 17
    parchis.avanzaPosiciones(2)
    assert parchis.fichaJ2 == 18
