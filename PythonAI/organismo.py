import math
import random

class Organismo:
    posX: int = 0
    posY: int = 0
    angulo: float = 0.0
    genoma = []
    estado: int = 0  # 0-Alive (-1)-Dead 1-Finish
    especie: int
    numero_miembro: int
    color: str = ""
    coefMutacion: float

    # default constructor
    def __init__(self, posX, posY, angulo, genoma, estado, especie, numero_miembro, coefMutacion, color):
        self.posX = posX
        self.posY = posY
        self.angulo = angulo
        self.genoma = genoma
        self.estado = estado
        self.color = color
        self.especie = especie
        self.numero_miembro = numero_miembro
        self.coefMutacion = coefMutacion

    def reset(self):
        self.posX = 0
        self.posY = 0
        self.angulo = 0
        self.estado = 0

    def mover(self, giro):
        self.angulo = self.angulo + self.genoma[giro]
        self.posX = self.posX + int(2 * math.cos(self.angulo))
        self.posY = self.posY + int(2 * math.sin(self.angulo))

    def get_genoma_value(self, index):
        return self.genoma[index]

    def get_genoma(self):
        return self.genoma

    def set_genoma(self, genomaAux):
        for x in range(0, genomaAux.__len__()):
            self.genoma[x] = genomaAux[x]

    def hijo(self, madre, padre, coefMutacion):
        random1: float = 0.0
        random2: float = 0.0
        len_genoma = self.genoma.__len__()
        self.genoma.clear()
        for x in range(len_genoma):
            random1 = random.uniform(0, 1)
            if random1 < 0.5:
                #self.genoma.remove(x)
                #self.genoma.insert(x, float(madre[x]))
                self.genoma.append(float(madre[x]))
            else:
                #self.genoma.remove(x)
                #self.genoma.insert(x, float(padre[x]))
                self.genoma.append(float(padre[x]))

            random2 = random.uniform(0, 1)

            if random2 < coefMutacion:
                self.genoma[x] = random.uniform(-0.2, 0.2)

    def compareTo(self, o):
        return self.angulo-o.angulo