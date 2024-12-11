import mcpi.minecraft as minecraft  #Llibreria de minecraft
from threading import Thread
import time
from insultBot import insultBot
from tnnnntBot import tntBot
from oracleBot import oracleBot

mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecraft

class BotManager:
    def __init__(self):
        self.botList = []

    def addBots(self, bot):
        self.botList.append(bot)

    def returnIndexActive(self, message):
        commandList = [bot.comandActive for bot in self.botList]
        isCommand = message in commandList
        if (isCommand):
            index = commandList.index(message)
            return index
        else :
            return -1
        
    def returnIndexEnd(self, message):
        commandList = [bot.comandEnd for bot in self.botList]
        isCommand = message in commandList
        if (isCommand):
            index = commandList.index(message)
            return index
        else :
            return -1

    def createThread(self, bot, playerId):
        #mc.postToChat("Creating Thread")
        bot.setPlayerId(playerId)
        thread = Thread(target=bot.iniBot)#, args=(playerId))
        thread.start()

    def showInfo(self):
        for x in self.botList:
            x.seeBot()

    def notifyBots(self, message):
        for x in self.botList:  #Per cada Bot
            if x.ini:  x.notify(message) #El notifiquem si esta actiu

    def comands(self, message):
        if message == "#stopBots": 
            for x in self.botList:
                x.ini = False
        elif message == "#showBots":  #En cas de showBots mostrem per pantalla tots els bots que pot controlar el manegador
            self.showInfo()
        elif message == "#showActiveBots":
            for x in self.botList:
                if x.ini: x.seeBot()
        else:
            msg = message.split(" ")
            if len(msg) == 2 and msg[0] == "#showInsults":
                try:
                    nameList = [bot.name for bot in self.botList]
                    index = nameList.index(msg[1])
                    mc.postToChat(f"<System> {self.botList[index].showInsults()}")
                except ValueError:
                    mc.postToChat(f"<System> {msg[1]} is not a correct Bot")
                #except AttributeError:
                    #mc.postToChat(f"<System> {msg[1]} is not a insult Bot")
                

    def checkChat(self, chatEvent):
        message = chatEvent.message  #Agafem el darrem missatge
        if message[0] == "#":  #Comprovem que s'hagi realitzat la comanda
            self.comands(message)
            indexA = self.returnIndexActive(message)
            if indexA >= 0:
                self.createThread(self.botList[indexA], chatEvent.entityId)
            indexE = self.returnIndexEnd(message)
            if indexE >= 0:
                self.botList[indexE].ini = False
        else :
            self.notifyBots(chatEvent)


    def startManaging(self):
        while True:
            time.sleep(1) 
            posts = mc.events.pollChatPosts()  #Obtenim els missatges que introdueix l'usuari pel chat
            if posts:
                for chat in posts:
                    self.checkChat(chat)
