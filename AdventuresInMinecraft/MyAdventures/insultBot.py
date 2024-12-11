import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecra
from fatherBot import fatherBot
import time
import random

class insultBot(fatherBot):
    insults = ["TONTO","CAP D'ESPINACA","INUTIL","LA TEVA PRACTICA ÉS TERRIBLE",
               "ETS TANT POC IMPORTANT QUE NO VAL LA PENA INSULTARTE"]

    def __init__(self, name, comandA, comandE):
        super().__init__(name, comandA, comandE)

    def iniBot(self):
        self.startBot()
        while self.ini:
            time.sleep(1)
            chat = self.accesChat()
            if len(chat) > 0:
                mc.postToChat(f"<{self.name}> {random.choice(self.insults)}")
                self.refresh()
        self.stopBot()

    def showInsults(self):
        return self.insults