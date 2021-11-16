class Individuo:
    x = 0
    y = 0
    puntaje = 0

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

    def setPuntaje(self, puntaje):
        self.puntaje = puntaje

    def getPuntaje(self):
        return self.puntaje
