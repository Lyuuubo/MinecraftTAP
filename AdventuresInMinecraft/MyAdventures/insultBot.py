from fatherBot import fatherBot
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecra
import time
import random

class insultBot(fatherBot):
    insults = ["TONTO","CAP D'ESPINACA","INUTIL"]

    def init(self, name, text):
        super().init(name, text)

    def iniBot(self):
        print(f"S'ha iniciat el bot: {self.name}")
        mc.postToChat(f"S'ha iniciat el bot: {self.name}")
        while True:
            time.sleep(2)
            chat = mc.events.pollChatPosts()
            if len(chat) > 0:
                mc.postToChat(f"<{self.name}> {random.choice(self.insults)}")
