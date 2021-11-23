import cv2
import Individuo
import numpy as np
from PIL import Image

img=cv2.imread("Prueba colores.png",1)

#FORMATO  img [Y, X]

B,G,R = img [49, 49]

#print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))


B,G,R = img [47, 46]

#print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))


B,G,R = img [0, 5]

#print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))

fix_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

fix_image[20:25, 10:20] = [255,255,255]

#cv2.imwrite("Prueba colores2.png", fix_image)

def pintarIndividuos(listaIndividuos, laberinto):
    #img=cv2.imread("laberinto-medium.png",1)

    if laberinto == "laberinto-easy":
        img = np.array(Image.open('laberinto-easy.png'))
    elif laberinto == "laberinto-medium":
        img = np.array(Image.open('laberinto-medium.png'))
    elif laberinto == "laberinto-hard":
        img = np.array(Image.open('laberinto-hard.png'))
    #img = np.array(Image.open('laberinto-easy.png'))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for i in listaIndividuos:
        if i.getColor() == 1 or i.getColor() == 2 or i.getColor() == 3:
            continue
        x = i.getX()
        y = i.getY()
        img[y,x] = [0,0,255*i.getPuntaje()/1000]

    if laberinto == "laberinto-easy":
        cv2.imwrite("laberinto-easy-Generacion.png", img)
    elif laberinto == "laberinto-medium":
        cv2.imwrite("laberinto-medium-Generacion.png", img)
    elif laberinto == "laberinto-hard":
        cv2.imwrite("laberinto-hard-Generacion.png", img)
    
    return

#print("prueba")
#img = np.array(Image.open('laberinto-easy.png'))
#print(img[25,25][0],img[25,25][1],img[25,25][2])
