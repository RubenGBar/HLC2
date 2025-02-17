from Boletin2.Ejercicio3 import calcularVDT

def test_VDT1():
    assert calcularVDT("D=32", "T=4") == "V=8"

def test_VDT2():
    assert calcularVDT("T=4", "V=8") == "D=32"

def test_VDT3():
    assert calcularVDT("V=8", "D=32") == "T=4"

def test_VDT4():
    assert calcularVDT("T=4", "D=32") == "V=8"

def test_VDT5():
    assert calcularVDT("D=32", "V=8") == "T=4"