from Individuo import *
import random
from pruebasColores import pintarIndividuos
import numpy as np
from PIL import Image

def validarPosicion(listaIndividuos, nuevoIndividuo):
    for individuo in listaIndividuos:
        if (individuo.getX() == nuevoIndividuo.getX() and individuo.getY() == nuevoIndividuo.getY()):
            return False
    return True

def PrimeraGeneracion(cantIndividuos, laberinto):
    if (cantIndividuos > 2500):
        return print("Cantidad de individuos inválida")
    listaIndividuos = []
    while cantIndividuos != 0:
        x = int(random.uniform(0,49))
        y = int(random.uniform(0,49))
        individuo = Individuo(x, y, 0)
        
        if (laberinto == 'laberinto-easy'):
            img = np.array(Image.open('laberinto-easy.png'))
        elif (laberinto == 'laberinto-medium'):
            img = np.array(Image.open('laberinto-medium.png'))
        elif (laberinto == 'laberinto-hard'):
            img = np.array(Image.open('laberinto-hard.png'))

        if img[y,x][0] == 0 and img[y,x][1] == 255 and img[y,x][2] == 0: # verde
            individuo.setColor(2)
            individuo.setPuntaje(1000)
        elif img[y,x][0] == 0 and img[y,x][1] == 0 and img[y,x][2] == 255: # azul
            individuo.setColor(3)
            individuo.setPuntaje(1000)
        elif img[y,x][0] == 255 and img[y,x][1] == 255 and img[y,x][2] == 255:
            individuo.setColor(0)
            individuo.setPuntaje(random.randint(50,200))
            #individuo.setPuntaje(1000)
        else:
            individuo.setColor(1)
            individuo.setPuntaje(0)

        if not (validarPosicion(listaIndividuos, individuo)):
            continue
        
        listaIndividuos.append(individuo)
        cantIndividuos -= 1

    for i in listaIndividuos:
        print("Posicion x: " + str(i.getX()) + ", Posicion Y: " + str(i.getY()))

    pintarIndividuos(listaIndividuos, laberinto)
    return listaIndividuos

#PrimeraGeneracion(70, 'laberinto-easy')

