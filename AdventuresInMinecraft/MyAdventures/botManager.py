from threading import Thread, Lock
import mcpi.minecraft as minecraft  #Llibreria de minecraft
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
                self.final = False
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
        for x in self.botList:      #Per cada Bot
            if x.ini:  x.notify(message.message)    #El notifiquem si esta actiu

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
            self.notifyBots(chatEvent)      #En cas de no ser una comanda notifiquem als bots

    def startManaging(self):
        while not self.final:
            time.sleep(1) 
            posts = mc.events.pollChatPosts()  #Obtenim els missatges que introdueix l'usuari pel chat
            if posts:
                for chat in posts:
                    self.checkChat(chat)

    def comands(self, mess):
        usedCommand = False
        message = mess.split(" ")
        command = message[0]
        if command == "#stopBots": 
            for x in self.botList:
                x.ini = False
            usedCommand = True
        elif command == "#showBots":  #En cas de showBots mostrem per pantalla tots els bots que pot controlar el manegador
            for bot in self.botList:
                name = ["name","comandActive","comandEnd"]
                bot.specificAttributes(name)
            usedCommand = True
        elif command == "#showActiveBots":
            name = ["name","comandActive","comandEnd"]
            for bot in self.botList:
                if bot.ini:  bot.specificAttributes(name)
            usedCommand = True
        elif command == '#showAttr':
            print("babunguers")
            if len(message) >= 2:
                indexN = self.returnIndexName(message[1])
                if indexN >= 0:
                    self.botList[indexN].allAttributes() 
                else: mc.postToChat(f"<System> Doesn't exist a bot with name: {message[1]}")
                usedCommand = True
            else: mc.postToChat(f"<System> Bad request (#showAttr nameBot)")
        elif command == '#showSpecificAttr':
            if len(message) >= 3:
                indexN = self.returnIndexName(message[1])
                if indexN >= 0:
                    self.botList[indexN].specificAttributes(message[2:]) 
                else: mc.postToChat(f"<System> Doesn't exist a bot with name: {message[1]}")
                usedCommand = True
            else: mc.postToChat(f"<System> Bad request (#showSpecificAttr nameBot att1 attr2 ...)")
        elif command == "#modifyAttribute":
            if len(message) != 4:
                mc.postToChat(f"<System> Bad request (#modifyAttribute nameBot attributeSelected newValue)")
            else:
                indexBot = self.returnIndexName(message[1])
                if (indexBot >= 0):
                    attributeSelected = message[2]
                    if (self.botList[indexBot].containsAttribute(attributeSelected)):
                        newValue = message[3]
                        value = self.botList[indexBot].modifyAttribute(attributeSelected, newValue)
                        print(value)
                        mc.postToChat(f"<System>  You have modified: {attributeSelected}" + f" His new value is: {value}")
                    else:
                       mc.postToChat(f"<System>  Doesn't exist an attribute named: {attributeSelected}")
                else:
                    mc.postToChat(f"<System> Doesn't exist a bot with that name: {message[1]}")  
            usedCommand = True
        return usedCommand  