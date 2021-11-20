class Individuo:
    x = 0
    y = 0
    puntaje = 0
    color = 0 #0. Blanco, 1. Negro, 2. Verde, 3. azul

    def __init__(self, x, y, puntaje):
        self.x = x
        self.y = y
        self.puntaje = puntaje

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPuntaje(self, puntaje):
        self.puntaje = puntaje

    def getPuntaje(self):
        return self.puntaje
