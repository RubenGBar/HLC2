from random import *

class Parchis:
    TAM_TABLERO = 20
    dado1 = 0
    dado2 = 0

    def __init__(self, nombreJ1, nombreJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nombreJ1 = nombreJ1
        self.nombreJ2 = nombreJ2

    @staticmethod
    def tiraDados():
        Parchis.dado1 = randint(1,6)
        Parchis.dado2 = randint(1,6)

    @staticmethod
    def pintaTablero(self):
        cad = ""
        i = 0
        j = 0
        k = 0

        while i <= Parchis.TAM_TABLERO:
            if i == 0:
                cad+=("\t" + "\tI")
            elif i == Parchis.TAM_TABLERO:
                cad+=("\t" + "F\n")
            else:
                cad+=("\t" + str(i))
            i += 1

        cad+=(self.nombreJ1 + "\tI")
        while j <= Parchis.TAM_TABLERO:
            if j == self.fichaJ1:
                cad+= "\tO"
            elif j == Parchis.TAM_TABLERO:
                cad+= "F\n"
            else:
                cad+= "\t"
            j += 1

        cad+=(self.nombreJ2 + "\tI")
        while k <= Parchis.TAM_TABLERO:
            if k == self.fichaJ2:
                cad+="\tO"
            elif k == Parchis.TAM_TABLERO:
                cad+="F\n"
            else:
               cad+= "\t"
            k += 1

        return cad

    def avanzaPosiciones(self, num):
        tirada = Parchis.dado1 + Parchis.dado2
        if num == 1:
            self.fichaJ1 += tirada
            if self.fichaJ1 > Parchis.TAM_TABLERO:
                self.fichaJ1 = Parchis.TAM_TABLERO - (self.fichaJ1 - Parchis.TAM_TABLERO)
        elif num == 2:
            self.fichaJ2 += tirada
            if self.fichaJ2 > Parchis.TAM_TABLERO:
                self.fichaJ2 = Parchis.TAM_TABLERO - (self.fichaJ2 - Parchis.TAM_TABLERO)

    def estadoCarrera(self):
        vaGanando = ""
        if self.fichaJ1 > self.fichaJ2:
            vaGanando = f"Va ganando {self.nombreJ1}"
        elif self.fichaJ1 < self.fichaJ2:
            vaGanando = f"Va ganando {self.nombreJ2}"
        else:
            vaGanando = f"{self.nombreJ1} y {self.nombreJ2} van empatados"
        return vaGanando

    def esGanador(self):
        ganador = ""
        if self.fichaJ1 == Parchis.TAM_TABLERO:
            ganador = f"{self.nombreJ1}"
        elif self.fichaJ2 == Parchis.TAM_TABLERO:
            ganador = f"{self.nombreJ2}"
        else:
            ganador = ""
        return ganador