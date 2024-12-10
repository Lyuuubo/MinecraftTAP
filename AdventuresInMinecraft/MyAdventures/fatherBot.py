import time
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecraft

class fatherBot:
    def __init__ (self, name, comandA, comandE):
        self.name = name   
        self.comandActive = comandA
        self.comandEnd = comandE
        self.chatList = []
        self.playerId = 0
        self.ini = False

    def setPlayerId(self, id):
        self.playerId = id
        print(f"Player id: {self.playerId}")

    def seeBot(self):
        print(f'Name: {self.name}')
        print(f"Activation commad: {self.comandActive}")
        print(f"Stop command: {self.comandEnd}")
        mc.postToChat(f'<System> Name: {self.name}')
        mc.postToChat(f"<System> Activation commad: {self.comandActive}")
        mc.postToChat(f"<System> Stop command: {self.comandEnd}")

    def stopBot(self):
        print(f'<System> You stop bot: {self.name}')
        mc.postToChat(f'<System> You stop bot: {self.name}')

    def startBot(self):
        self.ini = True
        print(f"<System> You started bot: {self.name}")
        mc.postToChat(f"<System> You started bot: {self.name}")
    
    def notify(self, message):
        self.chatList.append(message)

    def refresh(self):
        self.chatList.clear()

    def accesChat(self):
        return self.chatList

    def iniBot(self):
        pass

    def comp(self, text):
        return self.comand == text 