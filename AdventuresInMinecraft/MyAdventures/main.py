from botPare import botPare
from insultBot import insultBot
from patatBot import patatBot
import time
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecra


listBots = [insultBot("InsultBot","#insultBot"), patatBot("PatataBot","#patataBot")]
for bot in listBots:
    bot.seeBot()

while True:
    time.sleep(2)
    chat = mc.events.pollChatPosts()
    chat = [chatEvent.message for chatEvent in chat if chatEvent.message is not None]    #Per cada chatEvent que es troba a chat, agafem chatEvent.message
    if len(chat) > 0:
        comandList = [x.comand for x in listBots]
        isComand = chat[-1] in comandList
        print(isComand)
        if (isComand):
            index = comandList.index(chat[-1])
            print(index)
            listBots[index].iniBot()

