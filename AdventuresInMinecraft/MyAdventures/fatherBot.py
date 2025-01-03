from abc import ABC, abstractmethod
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecraft

class fatherBot(ABC):
    def __init__(self, name, comandA, comandE):
        self.name = name
        self.comandActive = comandA
        self.comandEnd = comandE
        self.chatList = []
        self.playerId = 0
        self.ini = False

    def setPlayerId(self, id):
        self.playerId = id
        print(f"Player id: {self.playerId}")

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

    @abstractmethod
    def iniBot(self):
        pass

    def comp(self, text):
        return self.comand == text
    
    def allAttributes(self):
        mc.postToChat(f'<System> Attr bot: {self.name}')
        for name, value in self.__dict__.items():
            mc.postToChat(f'  {name} : {value}')
            print(f'  {name} : {value}')

    def specificAttributes(self, values):
            mc.postToChat(f'<System> Attr bot: {self.name}')
            print(f'Attributes: {values}')
            for val in values:
                try:
                    attribute = getattr(self, val)
                    mc.postToChat(f'<System> {val} : {attribute}')
                except AttributeError as e:
                    print(e)
                    mc.postToChat(f"<System> Attribute with name ({val}) doesen't exist")

    def containsAttribute(self, value):
        return hasattr(self, value)
    
    def modifyAttribute(self, attribute, newValue):
        setattr(self, attribute, newValue)
        return newValue
