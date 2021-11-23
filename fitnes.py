from Individuo import *
import numpy as np
from PIL import Image
#from pruebasColores import pintarIndividuos
import random
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
def revisarParedes(x,y,lista,Ppuntaje):
      x2 = x-2
      puntaje = Ppuntaje
      while x2 < x+5:
            y2 = y-2
            while y2 != y+5:
                  try:
                        if lista[x2][y2].getColor1() == 1:
                              return 0
                        puntaje += lista[x2][y2].getPuntaje()
                  except:
                        ""
                  y2 += 1
            x2 += 1
      return puntaje

def revisarVecinos(x,y,lista):
      # x = 25, y = 25
      x2 = x-5
      puntaje = 0
      while x2 < x+5:
            y2 = y-5
            while y2 != y+5:
                  try:
                        puntaje += lista[x2][y2].getPuntaje()
                  except:
                        ""
                  y2 += 1
            x2 += 1
      return puntaje

def fitness(lista):
      x = 0
      while x != len(lista):
            y = 0
            while y != len(lista[0]):
                  if lista[x][y].getColor() == 0:
                        puntaje = revisarVecinos(x,y,lista)
                        puntaje = revisarParedes(x,y,lista,puntaje)
                        lista[x][y].setPuntaje(lista[x][y].getPuntaje()+(puntaje/100))
                  y += 1
            x += 1
      return lista

def revisarParedes(x,y,lista,Ppuntaje):
      x2 = x-2
      puntaje = Ppuntaje
      while x2 < x+5:
            y2 = y-2
            while y2 != y+5:
                  try:
                        if lista[x2][y2].getColor1() == 1:
                              return 0
                        puntaje += lista[x2][y2].getPuntaje()
                  except:
                        ""
                  y2 += 1
            x2 += 1
      return puntaje
                  
def generarIndividuos(laberinto):
      lista = []

      if laberinto == "laberinto-easy":
            img = np.array(Image.open('laberinto-easy.png'))
      elif laberinto == "laberinto-medium":
            img = np.array(Image.open('laberinto-medium.png'))

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
                        lista[x][y].setPuntaje(100)
                  else:
                        lista[x][y].setColor(1)
                        lista[x][y].setPuntaje(0)
      print(lista[25][25].getColor())
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

def Generaciones(kGeneraciones, laberinto):
      lista = generarIndividuos(laberinto)
      for i in range(kGeneraciones):
            fitness(lista)
      pintarIndividuos(lista, laberinto)

#Generaciones(10, "laberinto-medium")
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
            total += i.getPuntaje()
      for i in listaIndividuos:
            listaValores.append((i.getPuntaje() / total))
      return listaValores

#print(normalizarValores([30,23,51,11,3,8]))

def seleccion(listaIndividuos):
      listaValores = normalizarValores(listaIndividuos)
      listaProbabilidades = generarDistribucion(listaValores)
      listaSelec = []
      #for i in range(len(listaIndividuos)):
      #      listaSelec.append([])
      #print(listaProbabilidades)
      for i in range(len(listaIndividuos)):
            j = 0
            nRandom = random.random()
            print(nRandom)
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

def binarioADecimal(binario):
      binario = int(binario)
      decimal = 0
      i = 0
      while binario != 0:
            decimal += binario%10 * 2 ** i
            binario = binario//10
            i+=1
      return decimal

def generarParejas(listaIndividuos):
      listaParejas = []
      for i in range(0,len(listaIndividuos),2):  
            listaParejas.append(listaIndividuos[i:i+2])
      return listaParejas

def generarStringCruce(individuo):
      binIndividuo = agregarCeros(binarizar(individuo.getX()), 6) + agregarCeros(binarizar(individuo.getY()), 6)
      return binIndividuo

def validarMax49(individuo):
      if binarioADecimal(individuo[0:6]) <= 49 and binarioADecimal(individuo[6:]) <= 49:
            return True
      return False

def mutacion(individuo, indice):
      for i in range(indice):
            puntoMutacion = random.randint(0,11)
            if individuo[puntoMutacion] == "0":
                  individuo = individuo[:puntoMutacion] + "1" + individuo[puntoMutacion + 1:]
            else:
                  individuo = individuo[:puntoMutacion] + "0" + individuo[puntoMutacion + 1:]
            if not validarMax49(individuo):
                  i-=1
      return individuo

print(validarMax49("001010010110"))

def asignarNuevaPos(individuo, pos):
      individuo.setX(binarioADecimal(pos[0:6]))
      individuo.setY(binarioADecimal(pos[6:]))
      return

def cruce(listaParejas):
      nuevosIndiv = []
      for pareja in listaParejas:
            indiv1 = generarStringCruce(pareja[0])
            indiv2 = generarStringCruce(pareja[1])
            puntoCruce = random.randint(1,11)
            nuevoIndiv1 = indiv1[0:puntoCruce] + indiv2[puntoCruce:]
            nuevoIndiv2 = indiv2[0:puntoCruce] + indiv1[puntoCruce:]
            nuevoIndiv1 = mutacion(nuevoIndiv1, 1)
            nuevoIndiv2 = mutacion(nuevoIndiv2, 1)
            print(nuevoIndiv1)
            print(nuevoIndiv2)
            asignarNuevaPos(pareja[0], nuevoIndiv1)
            asignarNuevaPos(pareja[1], nuevoIndiv2)
            nuevosIndiv.append(pareja[0])
            nuevosIndiv.append(pareja[1])
      #print(nuevosIndiv[0].getX(), nuevosIndiv[0].getY())
      #print(nuevosIndiv[1].getX(), nuevosIndiv[1].getY())
      return nuevosIndiv


#print(cruce([[Individuo(10,20,20), Individuo(15,30,10)]]))

def generacion(listaIndividuos):
      listaSelec = seleccion(listaIndividuos)
      listaParejas = generarParejas(listaSelec)
      nuevaGeneracion = cruce(listaParejas)
      return nuevaGeneracion


#print(generacion([30,23,51,11,3,8]))
print(generacion([Individuo(10,20,20), Individuo(15,30,10)]))





    




                  
