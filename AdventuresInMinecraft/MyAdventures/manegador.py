import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecraft
import time
from provaInsultBot import insultBot
from botPare import botPare

class Manegador:
    def __init__(self):
        self.myListBot = []

    def addBot(self, bot):
        self.myListBot.append(bot)
    
    def mostrarBots(self):
        for x in self.myListBot:
            print(x.seeBot())

#main
#m = Manegador()
#m.addBot(insultBot("insultBot1","#insultBot1"))
#m.mostrarBots()