import unittest
from parchis.Parchis import Parchis

def test_estadoCarrera():
    parchis = Parchis("Juan", "Pepe")
    parchis.fichaJ1 = 10
    parchis.fichaJ2 = 5
    assert parchis.estadoCarrera() == "Va ganando Juan"

def test_estadoCarrera2():
    parchis = Parchis("Juan", "Pepe")
    parchis.fichaJ1 = 5
    parchis.fichaJ2 = 10
    assert parchis.estadoCarrera() == "Va ganando Pepe"

def test_estadoCarrera3():
    parchis = Parchis("Juan", "Pepe")
    parchis.fichaJ1 = 10
    parchis.fichaJ2 = 10
    assert parchis.estadoCarrera() == "Juan y Pepe van empatados"