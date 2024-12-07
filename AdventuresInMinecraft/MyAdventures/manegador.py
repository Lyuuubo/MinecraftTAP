import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecraft
import time

class Manegador:
    def __init__(self):
        self.perro = "perro"
        pass

m = Manegador()
print(m.perro)