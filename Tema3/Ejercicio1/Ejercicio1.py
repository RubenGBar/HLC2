abcdario = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def cifradoCesar(frase, num):
    fraseCodificada = ""
    mover = num%27
    i = 0

    for letra in frase:
        if letra != " " :
            i = abcdario.index(letra)
            fraseCodificada += abcdario[i+mover]
            i += i+1

    return fraseCodificada