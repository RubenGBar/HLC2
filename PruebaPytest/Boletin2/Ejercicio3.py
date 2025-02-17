from tokenize import String

def calcularVDT(num1:String, num2:String):

    res = 0
    num1Arraay = num1.split("=")
    num2Arraay = num2.split("=")
    letra1 = num1Arraay[0]
    letra2 = num2Arraay[0]
    valor1 = int(num1Arraay[1])
    valor2 = int(num2Arraay[1])
    resCad = ""

    if letra1 == "D" and letra2 == "T":
        res = valor1 / valor2
        res = int(res)
        resCad = "V=" + str(res)
    elif letra1 == "T" and letra2 == "D":
        res = valor2 / valor1
        res = int(res)
        resCad = "V=" + str(res)
    elif letra1 == "T" and letra2 == "V":
        res = valor1 * valor2
        res = int(res)
        resCad = "D=" + str(res)
    elif letra1 == "V" and letra2 == "D":
        res = valor2 / valor1
        res = int(res)
        resCad = "T=" + str(res)
    elif letra1 == "D" and letra2 == "V":
        res = valor1 / valor2
        res = int(res)
        resCad = "T=" + str(res)

    return resCad