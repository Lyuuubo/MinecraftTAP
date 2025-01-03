import mcpi.minecraft as minecraft  #Llibreria de minecraft

mc = minecraft.Minecraft.create()   #Crea connexiÃ³ amb minecraft

mc.player.setting("autojump", True)
while True:
    post = mc.events.pollChatPosts()
    if len(post) > 0:
        print(post)
        print(post[0].entityId)
        print(mc.getPlayerEntityId("Lyuuubo"))
        print(mc.entity.getPos(post[0].entityId))
        mc.postToChat("Mensaje para Lyuuubo: perro")