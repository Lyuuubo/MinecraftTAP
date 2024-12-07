import mcpi.minecraft as minecraft  #Llibreria de minecraft
import threading
import time

mc = minecraft.Minecraft.create()   #Crea connexió amb minecraft

class botManager:
    #botList=""
    botList=["insultBot"]
    def __init__(self):
        pass
    def showBots(self, mc):
        mc.postToChat(f'{self.botList}')
        
    def switch(self, message):
        if (message in self.botList):
            pass

    def hola(self):
        print("hola")

f = botManager()
while True:
    time.sleep(2) 
    posts = mc.events.pollChatPosts()  # Obtenim els missatges que introdueix l'usuari pel chat
    if posts:
        chat = [chatEvent.message for chatEvent in posts if chatEvent.message is not None] #Per cada chatEvent que es troba a chat, agafem chatEvent.message
        lastMessage = chat[-1]
        if lastMessage[:1] == "#":
            f.contains(lastMessage[1:])
            