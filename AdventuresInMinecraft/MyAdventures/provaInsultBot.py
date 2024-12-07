from botPare import botPare
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecra
import time

class insultBot(botPare):

    def __init__(self, name, text):
        super().__init__(name, text)

    def iniBot(self):
        print("Kevin")
        print(f"S'ha iniciat el bot: {self.name}")
        mc.postToChat(f"S'ha iniciat el bot: {self.name} per l'usuari {mc.getPlayerEntityId('Lyuuubo')}")
        while True:
            time.sleep(2)
            chat = mc.events.pollChatPosts()
            chat = [chatEvent.message for chatEvent in chat if chatEvent.message is not None]
            print(chat)
            mc.postToChat(f"<{self.name}> Cap d'espinaca")



