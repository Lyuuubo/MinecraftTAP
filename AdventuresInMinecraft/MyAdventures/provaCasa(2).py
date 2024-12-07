import mcpi.minecraft as minecraft  #Llibreria de minecraft
import time

mc = minecraft.Minecraft.create()   #Crea connexió amb minecraft

while True:
    time.sleep(0.1)
    pos = mc.player.getTilePos()    #Obtenim posició del jugador
    if pos.x <= -159 and pos.z == 504:
        mc.postToChat("hola")
        mc.postToChat(f'Id jugador: {mc.getPlayerEntityId("R3YUL")}')
        mc.postToChat(f'Posicio jugador: {mc.player.getPos()}')
