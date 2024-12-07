from botPare import botPare
from provaInsultBot import insultBot
import time
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecra


i = [insultBot("InsultBot1","#insultBot1"), insultBot("InsultBot2","#insultBot2")]
i[0].seeBot()
i[1].seeBot()

while True:
    time.sleep(2)
    chat = mc.events.pollChatPosts()
    chat = [chatEvent.message for chatEvent in chat if chatEvent.message is not None]    #Per cada chatEvent que es troba a chat, agafem chatEvent.message
    if len(chat) > 0:
        if i[0].comp(chat[-1]):
            i[0].iniBot()

