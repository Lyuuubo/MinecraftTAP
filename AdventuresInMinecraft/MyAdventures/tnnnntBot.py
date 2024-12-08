import mcpi.minecraft as minecraft  #Llibreria de minecraft
from mcpi import block
mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecra
from fatherBot import fatherBot
import time
import random

class tntBot(fatherBot):
    def __init__(self, name, comandActive, comandEnd, duration, lvl):
        self.duration = duration
        self.lvl = lvl
        super().__init__(name, comandActive, comandEnd)

    def iniBot(self):
        self.startBot()
        tim = 1
        if self.lvl == 2: tim = 0.5
        elif self.lvl == 3: tim = 0.2
        elif self.lvl == 4: tim = 0.1
        mc.postToChat(f"<{self.name}> Level: {self.lvl}, time: {tim}")
        mc.postToChat(f"<{self.name}> You have 5 s to run. HAHAHAHA!!")
        time.sleep(5)
        start = time.time()
        while time.time() - start < self.duration and self.ini:
            time.sleep(tim)
            playerPos = mc.player.getPos()
            mc.setBlock(playerPos.x,playerPos.y+4,playerPos.z, block.TNT.id, 1)
            mc.setBlock(playerPos.x,playerPos.y+5,playerPos.z, block.FIRE.id)
        if (self.ini): mc.postToChat(f"<{self.name}> Congratulations!! You win the game")
        else: 
            mc.postToChat(f"<{self.name}> You are a looser") 
            self.stopBot()
        self.ini = False