import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecraft
import time

while True:
    time.sleep(2)
    chat = mc.events.pollChatPosts()
    chat = [chatEvent.message for chatEvent in chat if chatEvent.message is not None]    #Per cada chatEvent que es troba a chat, agafem chatEvent.message
    if len(chat) > 0:
        if (chat[-1] == "#botInsult"):
            print("Kevin")
            print(f"S'ha iniciat el bot: {chat[-1]}")
            mc.postToChat(f"S'ha iniciat el bot: {chat[-1]} per l'usuari {mc.getPlayerEntityId('R3YUL')}")
            while True:
                time.sleep(2)
                chat = mc.events.pollChatPosts()
                chat = [chatEvent.message for chatEvent in chat if chatEvent.message is not None]
                print(chat)
                if len(chat) > 0 and 'ta mare' in chat[-1]:
                     mc.postToChat("<Kevin> Calla")

            