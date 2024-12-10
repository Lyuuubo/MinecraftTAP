from botManager import BotManager
from tnnnntBot import tntBot
from oracleBot import oracleBot
from insultBot import insultBot

class botInitialization:
    def __init__(self):
        pass

    def initialization(self):
        f = BotManager()
        f.addBots(insultBot("insultBot", "#insultBot", "#endInsultBot1"))
        f.addBots(tntBot("tntBot", "#tntBot","#endTntBot", 30, 4))
        f.addBots(oracleBot("chatBot", "#chatBot", "#endChatBot"))
        print("Bots activats")
        f.showInfo()
        f.startManaging()
