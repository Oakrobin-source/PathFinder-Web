import math
import random


class Organismo:
    posX: int = 0
    posY: int = 0
    angulo: float = 0.0
    genoma: [float]
    estado: int = 0  # 0-Alive (-1)-Dead 1-Finish
    color: int = 0
    coefMutacion: float

    # default constructor
    def __init__(self, coefMutacion, color):
        self.posX = 0
        self.posY = 0
        self.angulo = 0
        self.genoma = [float] * 1000
        self.estado = 0
        self.color = color
        self.coefMutacion = coefMutacion

    def get_posX(self):
        return self.posX

    def set_posX(self, x):
        self.posX = x

    def get_posY(self):
        return self.posY

    def set_posY(self, y):
        self.posY = y

    def get_angulo(self):
        return self.angulo

    def set_angulo(self, angulo):
        self.angulo = angulo

    def get_estado(self):
        return self.posY

    def set_estado(self, estado):
        self.estado = estado

    def reset(self):
        self.posX = 0
        self.posY = 0
        self.angulo = 0
        self.estado = 0

    def mover(self, giro):
        self.angulo = self.angulo + self.genoma[giro]
        self.posX = self.posX + int(2 * math.cos(self.angulo))
        self.posY = self.posY + int(2 * math.sin(self.angulo))

    def random_genoma(self):
        for x in range(self.genoma.__len__()):
            self.genoma[x] = random.uniform(-0.2, 0.2)

    def get_genoma_value(self, index):
        return self.genoma[index]

    def get_genoma(self):
        return self.genoma

    def set_genoma(self, genomaAux):
        for x in range(0, genomaAux.__len__()):
            self.genoma[x] = genomaAux[x]

    def hijo(self, madre, padre):
        random1: float = 0.0
        random2: float = 0.0

        for x in range(0, self.genoma.__len__()):
            random1 = random.uniform(0, 1)
            if random1 < 0.5:
                self.genoma[x] = madre.get_genoma_value(x)
            else:
                self.genoma[x] = padre.get_genoma_value(x)

            random2 = random.uniform(0, 1)

            if random2 < madre.coefMutacion:
                self.genoma[x] = random.uniform(-0.2, 0.2)

    def compareTo(self, o):
        return self.angulo-o.angulo