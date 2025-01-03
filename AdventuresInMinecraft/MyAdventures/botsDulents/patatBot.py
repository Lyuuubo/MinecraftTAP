from fatherBot import fatherBot
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecra
import time
import random

class patatBot(fatherBot):
    def __init__(self, name, comand):
        super().__init__(name, comand)

    def iniBot(self):
        print(f"S'ha iniciat el bot: {self.name}")
        mc.postToChat(f"S'ha iniciat el bot: {self.name} per l'usuari {mc.getPlayerEntityId('Lyuuubo')}")
        mc.postToChat(f"<{self.name}> patataPerrona")
        time.sleep(5)
        mc.postToChat(f"<{self.name}> patataSupepPerrona")