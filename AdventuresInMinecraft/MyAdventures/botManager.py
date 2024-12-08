import mcpi.minecraft as minecraft  #Llibreria de minecraft
import threading
import time
from insultBot import insultBot
from tnnnntBot import tntBot

mc = minecraft.Minecraft.create()   #Crea connexió amb minecraft

class BotManager:
    def __init__(self):
        self.botList = []    #Llista de bots que el manegador/controlador
        pass

    def showBots(self, mc):
        mc.postToChat(f'{self.botList}')

    def addBots(self, bot):
        self.botList.append(bot)

    def returnIndex(self, message):
        commandList = [bot.comand for bot in self.botList]
        isCommand = message in commandList
        if (isCommand):
            index = commandList.index(message)
            return index
        else :
            return -1

    def createThread(self, bot, mc):
        mc.postToChat("Creating Thread")
        thread = threading.Thread(target=bot.iniBot)
        thread.start()

    def showInfo(self):
        for x in self.botList:
            x.seeBot()

    def startManaging(self):
        while True:
            time.sleep(2) 
            posts = mc.events.pollChatPosts()  #Obtenim els missatges que introdueix l'usuari pel chat
            if posts:
                chat = [chatEvent.message for chatEvent in posts if chatEvent.message is not None] #Per cada chatEvent que es troba a chat, agafem chatEvent.message
                lastMessage = chat[-1]  #Agafem el darrem missatge
                if lastMessage[:1] == "#":  #Comprovem que s'hagi realitzat la comanda
                    index = self.returnIndex(lastMessage)
                    #print(index)
                    if index >= 0:
                        #print(f"Bot: {index}")
                        self.createThread(self.botList[index], mc)
                if lastMessage == "#showBots":  #En cas de showBots mostrem per pantalla tots els bots que pot controlar el manegador
                    self.showInfo()

f = BotManager()
f.addBots(insultBot("insultBot1", "#insultBot1"))
f.addBots(insultBot("insultBot2", "#insultBot2"))
#f.addBots(tntBot("tntBot1", "#tntBot1", 30, 1))
#f.addBots(tntBot("tntBot2", "#tntBot2", 30, 2))
#f.addBots(tntBot("tntBot3", "#tntBot3", 30, 3))
f.addBots(tntBot("tntBot4", "#tntBot4", 30, 4))
f.showInfo()
f.startManaging()