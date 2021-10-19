import cv2

img=cv2.imread("Prueba colores.png",1)

#FORMATO  img [Y, X]

B,G,R = img [49, 49]

print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))


B,G,R = img [47, 46]

print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))


B,G,R = img [0, 5]

print("Rojo: R: " + str(R) + ", G: " + str(G) + ", B: " + str(B))