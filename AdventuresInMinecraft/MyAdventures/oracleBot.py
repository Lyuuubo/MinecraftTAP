from fatherBot import fatherBot
import mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecra
import google.generativeai as genai
import time

class oracleBot(fatherBot):
    def __init__(self, name, comandActive, comandEnd):
        super().__init__(name, comandActive, comandEnd)
        

    def iniBot(self):
        self.startBot()
        genai.configure(api_key='AIzaSyC7QN5XxtTguQK6CxrrCL9B1c6yo2IdF48')
        model = genai.GenerativeModel("gemini-1.5-flash")
        while self.ini:
            time.sleep(1)
            chat = self.accesChat()
            if len(chat) > 0:
                response = model.generate_content(str(chat[0].message))
                print(response.text)
                mc.postToChat(f"<{self.name}> {response.text}")
                self.refresh()
        self.stopBot()
