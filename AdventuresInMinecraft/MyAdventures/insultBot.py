import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecra
from fatherBot import fatherBot
import time
import random

class insultBot(fatherBot):
    insults = ["TONTO","CAP D'ESPINACA","INUTIL"]

    def init(self, name, comandA, comandE):
        super().init(name, comandA, comandE)

    def iniBot(self):
        print(f"S'ha iniciat el bot: {self.name}")
        mc.postToChat(f"<System> Started bot: {self.name}")
        while self.ini:
            time.sleep(1)
            chat = self.accesChat()
            if len(chat) > 0 and chat[-1] not in (self.comandActive, self.comandEnd):
                mc.postToChat(f"<{self.name}> {random.choice(self.insults)}")
                self.refresh()
        self.stopBot()