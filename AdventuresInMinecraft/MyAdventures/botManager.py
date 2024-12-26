import mcpi.minecraft as minecraft  #Llibreria de minecraft
from threading import Thread, Lock
import time

mc = minecraft.Minecraft.create()   #Crea connexió amb minecraft

class BotManager():
    instance = None
    lock: Lock = Lock()

    def __new__(self):
        with self.lock:
            if self.instance is None:
                self.instance = super().__new__(self)
                self.botList = []
        return self.instance

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
        
    def returnIndexName(self, name):
        nameList = [bot.name for bot in self.botList]
        isName = name in nameList
        if (isName):
            index = nameList.index(name)
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

    def checkChat(self, chatEvent):
        message = chatEvent.message  #Agafem el darrem missatge
        if message[0] == "#":  #Comprovem que s'hagi realitzat la comanda
            used = self.comands(message)
            if used is False:
                indexA = self.returnIndexActive(message)
                if indexA >= 0:
                    self.createThread(self.botList[indexA], chatEvent.entityId)
                else: 
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

    def comands(self, mess):
        usedCommand = False
        message = mess.split(" ")
        comanda = message[0]
        if comanda == "#stopBots": 
            for x in self.botList:
                x.ini = False
            usedCommand = True
        elif comanda == "#showBots":  #En cas de showBots mostrem per pantalla tots els bots que pot controlar el manegador
            for bot in self.botList:
                name = ["name","comandActive","comandEnd"]
                bot.specificAttributes(name)
            usedCommand = True
        elif comanda == "#showActiveBots":
            name = ["name","comandActive","comandEnd"]
            for bot in self.botList:
                if bot.ini:  bot.specificAttributes(name)
            usedCommand = True
        elif comanda == '#showAttr':
            if len(message) >= 2:
                indexN = self.returnIndexName(message[1])
                if indexN >= 0:
                    self.botList[indexN].allAttributes() 
                else: mc.postToChat(f"<System> Doesen't exist a bot with name: {message[1]}")
                usedCommand = True
            else: mc.postToChat(f"<System> Bad request (#showAttr nameBot)")
        elif comanda == '#showSpecificAttr':
            if len(message) >= 3:
                indexN = self.returnIndexName(message[1])
                if indexN >= 0:
                    self.botList[indexN].specificAttributes(message[2:]) 
                else: mc.postToChat(f"<System> Doesen't exist a bot with name: {message[1]}")
                usedCommand = True
            else: mc.postToChat(f"<System> Bad request (#showSpecificAttr nameBot att1 attr2 ...)")
        return usedCommand  