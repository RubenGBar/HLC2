from Ejercicio4 import kaprekar

# Test para comprobar que el algoritmo funciona con el ejemplo proporcionado en el ejercicio
# Resultado:
def test_kaprekar():
    assert kaprekar(1121) == 5

# Test para comprobar que me ordenaba bien el número más grande posible, por lo que solo se puede realizar en un momento específico
# Resultado: Correcto
def test_kaprekar2():
    assert kaprekar(2134) == 4321

# Test para comprobar que me ordenaba bien el número más pequeño posible, por lo que solo se puede realizar en un momento específico
# Resultado: Correcto
def test_kaprekar3():
    assert kaprekar(2134) == 1234

# Test para comprobar que el resultado de la resta es correcto, por lo que solo se puede realizar en un momento específico
# Resultado: Correcto
def test_kaprekar4():
    assert kaprekar(2134) == 3087

# Test para comprobar que el algoritmo no pare hasta que me devuelva 6174, por lo que solo se puede realizar en un momento específico
# Resultado:
def test_kaprekar5():
    assert kaprekar(2134) == 6174

# Test para comprobar que el algoritmo funciona
# Resultado:
def test_kaprekar6():
    assert kaprekar(2134) == 3
