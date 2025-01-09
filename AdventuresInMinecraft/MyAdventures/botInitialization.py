from threading import Thread
from botManager import BotManager
from tnnnntBot import tntBot
from oracleBot import oracleBot
from insultBot import insultBot
import mcpi.minecraft as minecraft  #Llibreria de minecraft

mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecraft

class botInitialization:
    def __init__(self):
        self.f = BotManager()
        pass

    def initialization(self):
        self.f.addBots(insultBot("insultBot1", "#insultBot1", "#endInsultBot1"))
        self.f.addBots(insultBot("insultBot2", "#insultBot2", "#endInsultBot2"))
        # #f.addBots(tntBot("tntBot1", "#tntBot1", 30, 1))
        # #f.addBots(tntBot("tntBot2", "#tntBot2", 30, 2))
        # #f.addBots(tntBot("tntBot3", "#tntBot3", 30, 3))
        self.f.addBots(tntBot("tntBot", "#tntBot","#endTntBot", 30, 4))
        self.f.addBots(oracleBot("chatBot", "#chatBot", "#endChatBot"))
        # #f.showInfo()
        thread = Thread(target=self.f.startManaging)#, args=(playerId))
        thread.start()
    
    def finalManaging(self):
        self.f.final = True

bot = botInitialization()
bot.initialization()