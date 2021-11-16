from Individuo import *
from random import randint
from pruebasColores import pintarIndividuos

def validarPosicion(listaIndividuos, nuevoIndividuo):
    for individuo in listaIndividuos:
        if (individuo.getX() == nuevoIndividuo.getX() and individuo.getY() == nuevoIndividuo.getY()):
            return False
    return True

def PrimeraGeneracion(cantIndividuos):
    if (cantIndividuos > 2500):
        return print("Cantidad de individuos inválida")
    listaIndividuos = []
    while cantIndividuos != 0:
        x = randint(0,49)
        y = randint(0,49)
        individuo = Individuo(x, y, 0)

        if not (validarPosicion(listaIndividuos, individuo)):
            continue
        
        listaIndividuos.append(individuo)
        cantIndividuos -= 1

    for i in listaIndividuos:
        print("Posicion x: " + str(i.getX()) + ", Posicion Y: " + str(i.getY()))

    pintarIndividuos(listaIndividuos)
    return

PrimeraGeneracion(70)

