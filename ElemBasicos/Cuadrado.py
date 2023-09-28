class Cuadrado:
    def __init__(self,posX, posY,tam,color):
        self.posX = posX
        self.posY = posY
        self.tam = tam
        self.color = color
        self.velx = 1
        self.vely = 1
        pass
    pass
    def comprobarL(self,maxX, maxY):
        if (self.posX + self.tam) >= maxX:
            self.velx = -1
            print("Limite X >:",self.posX )
        if (self.posY + self.tam) >= maxY:
            self.vely = -1
            print("Limite Y >:",self.posY )
        if self.posX  <= 0:
            self.velx = 1
            print("Limite X >:",self.posX )
        if self.posY <= 0:
            self.posY = 5
            self.vely = 1
            print("Limite Y >:",self.posY )
        pass