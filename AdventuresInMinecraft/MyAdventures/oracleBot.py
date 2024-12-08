from fatherBot import fatherBot
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecra
import google.generativeai as genai
import time

class oracleBot(fatherBot):
    def __init__(self, name, comandActive, comandEnd):
        super().__init__(name, comandActive, comandEnd)
        

    def iniBot(self):
        print(f"S'ha iniciat el bot: {self.name}")
        mc.postToChat(f"S'ha iniciat el bot: {self.name}")
        genai.configure(api_key='')
        model = genai.GenerativeModel("gemini-1.5-flash")
        while self.ini:
            time.sleep(1)
            chat = self.accesChat()
            if len(chat) > 0 and chat[-1] not in (self.comandActive, self.comandEnd):
                response = model.generate_content(str(chat))
                mc.postToChat(f"<{self.name}> {response.text}")
                self.refresh()
        self.stopBot()
