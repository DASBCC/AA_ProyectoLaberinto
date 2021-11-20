from Individuo import *
import numpy as np
from PIL import Image
from pruebasColores import pintarIndividuos
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
                        lista[x][y].setPuntaje(lista[x][y].getPuntaje()+(puntaje/100))
                  y += 1
            x += 1
      return lista
                  
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
















                  
