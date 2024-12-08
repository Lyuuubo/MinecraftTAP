import time
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecraft

class fatherBot:
    def __init__ (self, name, comandA, comandE):
        self.name = name   
        self.comandActive = comandA
        self.comandEnd = comandE
        self.chatList = []
        self.ini = False

    def seeBot(self):
        print(f'Nom: {self.name}')
        print(f"Comanda d'activacio: {self.comandActive}")
        print(f"Comanda desactivacio: {self.comandEnd}")
        mc.postToChat(f'Nom: {self.name}')
        mc.postToChat(f"Comanda d'activacio: {self.comandActive}")
        mc.postToChat(f"Comanda desactivacio: {self.comandEnd}")

    def stopBot(self):
        print(f'<System> You stop bot: {self.name}')
        mc.postToChat(f'<System> You stop bot: {self.name}')
    
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