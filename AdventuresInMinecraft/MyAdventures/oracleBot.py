import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from MyAdventures.fatherBot import fatherBot
import MyAdventures.mcpi.minecraft as minecraft  #Llibreria de minecraft
mc = minecraft.Minecraft.create()   #Crea connexió amb minecra
import google.generativeai as genai
import time

class oracleBot(fatherBot):
    def __init__(self, name, comandActive, comandEnd):
        super().__init__(name, comandActive, comandEnd)

    #Mètode abstracte del pare
    def iniBot(self):
        self.startBot()
        genai.configure(api_key='AIzaSyAiwmxgeQvufzHZ_XnDhbKQ92Iwfe_KOCs')
        model = genai.GenerativeModel("gemini-1.5-flash")
        while self.ini:
            time.sleep(1)
            chat = self.accesChat()
            if len(chat) > 0:
                try:
                    mc.postToChat(f"<{self.name}> ...")
                    response = model.generate_content(str(chat[0]))
                    self.printText(response)
                except Exception as e:
                    #print(e)
                    mc.postToChat(f"<{self.name}> Error with this request")
                self.refresh()
        self.stopBot()

    def printText(self, response):
            #print(f"<{self.name}> {response.text}")
            responseFract = response.text.split("\n")
            #responseFract = responseFract[0:-1]
            for text in responseFract:
                if not self.ini:
                    break
                time.sleep(2)
                #print(text)
                if len(text) == 0:
                    mc.postToChat(f"{text}")
                else:
                    mc.postToChat(f"<{self.name}> {text}")
            mc.postToChat(f"<{self.name}> End message")
        #mc.postToChat(f"<{self.name}> {response.text}") 