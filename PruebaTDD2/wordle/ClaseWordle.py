from random import randint

class ClaseWordle:
    palabras = ["ANGEL", "JAMON", "LENTO", "VERDE", "PLAYA", "HIELO", "FUEGO", "MANGO", "BANCO", "SALTO"]

    def __init__(self):
        self.palabraJuego = ""
        self.pistas = [["-----", "-----"], ["-----", "-----"], ["-----", "-----"], ["-----", "-----"], ["-----", "-----"], ["-----", "-----"]]
        self.numIntento = 0;

    def seleccionaJuego(self):
        num = randint(0, len(ClaseWordle.palabras))
        self.palabraJuego = ClaseWordle.palabras[num]

    def realizaIntento(self, intento):
        for j in range(len(self.pistas[self.numIntento])):
            self.pistas[self.numIntento][0] = intento
            cadenaConPistas = ""
            for k in range(len(self.pistas[self.numIntento][j])):
                if intento[k] == self.palabraJuego[k]:
                    cadenaConPistas += intento[k]
                elif str(intento[k]) in self.palabraJuego:
                    cadenaConPistas += "*"
                else:
                    cadenaConPistas += "-"
            self.pistas[self.numIntento][1] = cadenaConPistas
        self.numIntento += 1

    # ME HE QUEDADO POR HACER LA FUNCION DE ACERTADO Y PINTAPISTAS