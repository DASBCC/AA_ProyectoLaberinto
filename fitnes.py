from Individuo import *
import numpy as np
from PIL import Image
from pruebasColores import pintarIndividuos
import random
from GeneracionAuto import PrimeraGeneracion
"""
def revisarVecinos(x,y,lista):
      # x = 25, y = 25
      x2 = x-7
      puntaje = 0
      while x2 < x+7:
            y2 = y-7
            while y2 != y+7:
                  try:
                        puntaje += lista[x2][y2].getPuntaje()
                  except:
                        ""
                  y2 += 1
            x2 += 1
      return puntaje
"""

def revisarVecinos(individuo,lista):
      # x = 25, y = 25
      x2 = individuo.getX-5
      puntaje = 0
      conta = 0
      while x2 < individuo.getX()+5:
            y2 = individuo.getY-5
            while y2 != individuo.getY()+5:
                  for i in lista:
                        if i != individuo:
                              if i.getX() == x2 and i.getY() == y2:
                                    puntaje = puntaje + i.getPuntaje()
                                    conta += 1
                  y2 += 1
            x2 += 1
      if conta!=0:
            return puntaje/conta
      return individuo.getPuntaje


def revisarParedes(individuo,puntaje,laberinto):
      x = individuo.getX()
      y = individuo.getY()
      if laberinto == "laberinto-easy":
            img = np.array(Image.open('laberinto-easy.png'))
      elif laberinto == "laberinto-medium":
            img = np.array(Image.open('laberinto-medium.png'))
      elif laberinto == "laberinto-hard":
            img = np.array(Image.open('laberinto-hard.png'))
      cont = 0
      try:
            x -= 5
            if img[y,x][0] == 0 and img[y,x][1] == 0 and img[y,x][2] == 0:
                  cont += 1
            x += 10
            if img[y,x][0] == 0 and img[y,x][1] == 0 and img[y,x][2] == 0:
                  cont += 1
            x -= 5
            y -= 5
            if img[y,x][0] == 0 and img[y,x][1] == 0 and img[y,x][2] == 0:
                  cont += 1
            y += 10
            if img[y,x][0] == 0 and img[y,x][1] == 0 and img[y,x][2] == 0:
                  cont += 1
      except:
            ""
      puntaje = puntaje*0.85
      return puntaje
def fitness(lista,laberinto):
      puntaje = 0
      for i in lista:
            if i.getColor == 0:
                 puntaje = revisarVecinos(i,lista)
                 puntaje = revisarParedes(i,puntaje,laberinto)
                 i.setPuntaje(puntaje)
                  
def generarIndividuos(laberinto):
      lista = []

      if laberinto == "laberinto-easy":
            img = np.array(Image.open('laberinto-easy.png'))
      elif laberinto == "laberinto-medium":
            img = np.array(Image.open('laberinto-medium.png'))
      elif laberinto == "laberinto-hard":
            img = np.array(Image.open('laberinto-hard.png'))

      for x in range(50):
            lista.append([])
            for y in range(50):
                  lista[x].append(Individuo(x, y, 0))
                  if img[y,x][0] == 0 and img[y,x][1] == 255 and img[y,x][2] == 0: # verde
                        lista[x][y].setColor(2)
                        lista[x][y].setPuntaje(1000)
                  elif img[y,x][0] == 0 and img[y,x][1] == 0 and img[y,x][2] == 255: # azul
                        lista[x][y].setColor(3)
                        lista[x][y].setPuntaje(1000)
                  elif img[y,x][0] == 255 and img[y,x][1] == 255 and img[y,x][2] == 255:
                        lista[x][y].setColor(0)
                        lista[x][y].setPuntaje(randint(0,100))
                  else:
                        lista[x][y].setColor(1)
                        lista[x][y].setPuntaje(0)
      return lista

#generarIndividuos("laberinto-easy")

def generarTemporal():
      lista = []
      for x in range(50):
            lista.append([])
            for y in range(50):
                  lista[x].append(Individuo(x, y, 0))
                  if 20 <= x <= 32 and 2 <= y <= 12: # verde
                        lista[x][y].setColor(2)
                        lista[x][y].setPuntaje(1000)
                  elif 20 <= x <= 32 and 38 <= y <= 48: # rojo
                        lista[x][y].setColor(3)
                        lista[x][y].setPuntaje(1000)
                  elif 20 < x < 32 and 11 < y < 38:
                        lista[x][y].setColor(0)
                        lista[x][y].setPuntaje(100)
                  else:
                        lista[x][y].setColor(1)
                        lista[x][y].setPuntaje(0)
      return lista

def Generaciones(kGeneraciones, cantIndividuos, laberinto):
      #lista = generarIndividuos(laberinto)
      lista = PrimeraGeneracion(cantIndividuos,laberinto)
      for i in range(kGeneraciones):
            alterGeneracion(lista, laberinto)
            fitness(lista,laberinto)
            print("Generación #" + str(i+1))
      pintarIndividuos(lista, laberinto)

Generaciones(10, "laberinto-medium")
"""
lista = generarTemporal()

                        
                  
lista = fitness(lista)
lista = fitness(lista)
lista = fitness(lista)
i = 0
while i != len(lista[0]):
      j = 0
      while j != len(lista):
            print(lista[j][i].getPuntaje(),lista[j][i].getX(),lista[j][i].getY(),lista[j][i].getColor())
            j += 1
      i += 1
"""




#DISTRIBUCIÓN DE PROBABILIDADES

def generarDistribucion(lista):
      listaDist = []
      for i in range(len(lista)):
            listaDist.append([])

      temp = 0
      for i in range(len(lista)):
            listaDist[i] = ((temp , temp + lista[i]))
            temp = temp + lista[i]

      return listaDist

def normalizarValores(listaIndividuos):
      total = 0
      listaValores = []
      for i in listaIndividuos:
            total += i
      for i in listaIndividuos:
            listaValores.append((i / total))
      return listaValores

#print(normalizarValores([30,23,51,11,3,8]))

def seleccion(listaIndividuos):
      listaValores = normalizarValores(listaIndividuos)
      listaProbabilidades = generarDistribucion(listaValores)
      listaSelec = []
      #for i in range(len(listaIndividuos)):
      #      listaSelec.append([])
      print(listaProbabilidades)
      for i in range(len(listaIndividuos)):
            j = 0
            nRandom = random.random()
            #print(nRandom)
            for probabilidad in listaProbabilidades: 
                  if probabilidad[0] <= nRandom < probabilidad[1]:
                        listaSelec.append(listaIndividuos[j])
                        break
                  j+=1
      return listaSelec

def binarizar(decimal):
    """
    Funcionalidades: Convierte un numero a su forma binaria
    Entradas: int decimal
    Salidas: string con el número convertido a binario
    """
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def agregarCeros(num, cantDigitos):
    """
    Funcionalidades: Agrega los 0 a la izquierda faltantes en función a la cantidad de bits original del número
    Entradas: int num, int cantDigitos
    Salidas: string con el número final
    """
    numStr = str(num)
    while (len(numStr) < cantDigitos):
        numStr = "0" + numStr
    return numStr

def generarParejas(listaIndividuos):
      listaParejas = []
      for i in range(0,len(listaIndividuos),2):  
            listaParejas.append(listaIndividuos[i:i+2])
      return listaParejas

def generarStringCruce(individuo):
      binIndividuo = agregarCeros(binarizar(individuo.getX()), 6) + agregarCeros(binarizar(individuo.getY()), 6)
      return binIndividuo

<<<<<<< Updated upstream
def validarMax49(individuo):
      if binarioADecimal(individuo[0:6]) <= 49 and binarioADecimal(individuo[6:]) <= 49:
            #print("x " + str(binarioADecimal(individuo[0:6])) + " y " + str(binarioADecimal(individuo[6:])))
            return True
      return False

def mutacion(individuo, indice):
      i = 0
      while i < indice:
            puntoMutacion = random.randint(0,11)
            if individuo[puntoMutacion] == "0":
                  individuo = individuo[:puntoMutacion] + "1" + individuo[puntoMutacion + 1:]
            else:
                  individuo = individuo[:puntoMutacion] + "0" + individuo[puntoMutacion + 1:]
            if not validarMax49(individuo):
                  i-=1
            i+=1
      return individuo

def asignarNuevaPos(individuo, pos):
      individuo.setX(binarioADecimal(pos[0:6]))
      individuo.setY(binarioADecimal(pos[6:]))
      return
def asignarColor(individuo, laberinto):
      x = individuo.getX()
      y = individuo.getY()
      
      if (laberinto == 'laberinto-easy'):
            img = np.array(Image.open('laberinto-easy.png'))
      elif (laberinto == 'laberinto-medium'):
            img = np.array(Image.open('laberinto-medium.png'))
      elif (laberinto == 'laberinto-hard'):
            img = np.array(Image.open('laberinto-hard.png'))

      if img[y,x][0] == 0 and img[y,x][1] == 255 and img[y,x][2] == 0: # verde
            individuo.setColor(2)
            #individuo.setPuntaje(1000)
      elif img[y,x][0] == 0 and img[y,x][1] == 0 and img[y,x][2] == 255: # azul
            individuo.setColor(3)
            #individuo.setPuntaje(1000)
      elif img[y,x][0] == 255 and img[y,x][1] == 255 and img[y,x][2] == 255:
            individuo.setColor(0)
            #si está en blanco el color se determinará en el fitness
      else:
            individuo.setColor(1)
            #individuo.setPuntaje(0)
      return

def cruce(listaParejas, laberinto):
      nuevosIndiv = []
      for pareja in listaParejas:
            indiv1 = generarStringCruce(pareja[0])
            indiv2 = generarStringCruce(pareja[1])
            puntoCruce = random.randint(1,11)
            print(puntoCruce)
            nuevoIndiv1 = indiv1[0:puntoCruce] + indiv2[puntoCruce:]
            nuevoIndiv2 = indiv2[0:puntoCruce] + indiv1[puntoCruce:]
            nuevosIndiv.append(nuevoIndiv1)
            nuevosIndiv.append(nuevoIndiv2)
            nuevoIndiv1 = mutacion(nuevoIndiv1, 1)
            nuevoIndiv2 = mutacion(nuevoIndiv2, 1)
            #print(nuevoIndiv1)
            #print(nuevoIndiv2)
            asignarNuevaPos(pareja[0], nuevoIndiv1)
            asignarNuevaPos(pareja[1], nuevoIndiv2)
            asignarColor(pareja[0], laberinto)
            asignarColor(pareja[1], laberinto)
            nuevosIndiv.append(pareja[0])
            nuevosIndiv.append(pareja[1])
      #print(nuevosIndiv[0].getX(), nuevosIndiv[0].getY())
      #print(nuevosIndiv[1].getX(), nuevosIndiv[1].getY())
      return nuevosIndiv

print(cruce([[Individuo(10,20,20), Individuo(15,30,10)]]))

def alterGeneracion(listaIndividuos, laberinto):
      listaSelec = seleccion(listaIndividuos)
      listaParejas = generarParejas(listaSelec)
      return listaParejas


print(generacion([30,23,51,11,3,8]))
      nuevaGeneracion = cruce(listaParejas, laberinto)
      return nuevaGeneracion


#print(generacion([30,23,51,11,3,8]))
#print(alterGeneracion([Individuo(10,20,20), Individuo(15,30,10)]))



                  
