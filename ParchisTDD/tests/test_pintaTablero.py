import unittest
from parchis.Parchis import Parchis

"""
Primer Test | 
Compruebo que la fila de arriba se dibuja bien
def test_pintaTablero():
    parchis = Parchis("Juan", "Pepe")
    assert parchis.pintaTablero(parchis) == "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\n"
Resultado: PASSED -> 07/11 10:53

Segundo Test | 
Compruebo que las dos primeras filas se dibujan bien
def test_pintaTablero():
    parchis = Parchis("Juan", "Pepe")
    assert (parchis.pintaTablero(parchis) == "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\nJuan\tI\tO\t\t\t\t\t\t\t\t\tF\n")
Resultado: PASSED -> 07/11 11:00

Tercer Test | 
Compruebo que se impriba bien todo el tablero
def test_pintaTablero():
    parchis = Parchis("Juan", "Pepe")
    assert (parchis.pintaTablero(parchis) == "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\nJuan\tI\tO\t\t\t\t\t\t\t\t\tF\nPepe\tI\tO\t\t\t\t\t\t\t\t\tF\n")
Resultado: PASSED -> 07/11 11:54

Cuarto Test |
Compruebo que el tablero se imprima bien con diferentes tamaños
def test_pintaTablero():
    parchis = Parchis("Juan", "Pepe")
    assert (parchis.pintaTablero(parchis) == "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\nJuan\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\nPepe\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n")
Resultado: PASSED -> 07/11 12:25

Quinto Test |
Compruebo que el tablero se imprima bien con las fichas en diferentes posiciones
def test_pintaTablero():
    parchis = Parchis("Juan", "Pepe")
    assert (parchis.pintaTablero(parchis) == "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\nJuan\tI\t\t\t\t\t\t\t\tO\t\tF\nPepe\tI\t\t\t\t\t\tO\t\t\t\tF\n")
Resultado: PASSED -> 07/11 12:30

"""

def test_pintaTablero():
    parchis = Parchis("Juan", "Pepe")
    parchis.TAM_TABLERO = 10
    assert (parchis.pintaTablero(parchis) == "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\nJuan\tI\tO\t\t\t\t\t\t\t\t\tF\nPepe\tI\tO\t\t\t\t\t\t\t\t\tF\n")

def test_pintaTablero2():
    parchis = Parchis("Juan", "Pepe")
    parchis.TAM_TABLERO = 20
    assert (parchis.pintaTablero(parchis) == "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\nJuan\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\nPepe\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n")

def test_pintaTableroPosDiferentes():
    parchis = Parchis("Juan", "Pepe")
    parchis.TAM_TABLERO = 10
    parchis.fichaJ1 = 7
    parchis.fichaJ2 = 5
    assert (parchis.pintaTablero(parchis) == "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\nJuan\tI\t\t\t\t\t\t\t\tO\t\tF\nPepe\tI\t\t\t\t\t\tO\t\t\t\tF\n")
