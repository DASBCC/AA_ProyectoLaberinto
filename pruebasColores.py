import cv2
import Individuo

img=cv2.imread("Prueba colores.png",1)

#FORMATO  img [Y, X]

B,G,R = img [49, 49]

print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))


B,G,R = img [47, 46]

print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))


B,G,R = img [0, 5]

print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))

fix_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

fix_image[20:25, 10:20] = [255,255,255]

cv2.imwrite("Prueba colores2.png", fix_image)

def pintarIndividuos(listaIndividuos):
    img=cv2.imread("laberinto-medium.png",1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for i in listaIndividuos:
        x = i.getX()
        y = i.getY()
        img[x,y] = [255,0,0]

    cv2.imwrite("Prueba pintar generacion.png", img)
    return

