import time
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecraft

class fatherBot:
    def __init__ (self, name, comand):
        self.name = name
        self.comand = comand
        self.ini = False

    def seeBot(self):
        print(f'Nom: {self.name}')
        print(f"Comanda d'activacio: {self.comand}")
        mc.postToChat(f'Nom: {self.name}')
        mc.postToChat(f"Comanda d'activacio: {self.comand}")

    def iniBot(self):
        pass

    def comp(self, text):
        return self.comand == text  