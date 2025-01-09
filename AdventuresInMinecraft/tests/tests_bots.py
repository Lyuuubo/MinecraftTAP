from collections import deque
import os
import sys
import time
from threading import Thread
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)    

from MyAdventures.tnnnntBot import tntBot
from MyAdventures.insultBot import insultBot
from MyAdventures.oracleBot import oracleBot

class TestMan(unittest.TestCase):

    #Comprovem funcionalitat insultBot
    def test_insultBot(self):
        print("test_insultBot")
        bot = insultBot("insultBot1","#insultBot1","#endInsultBot1")
        self.assertEqual("insultBot1", bot.name)
        self.assertEqual("#insultBot1", bot.comandActive)
        self.assertEqual("#endInsultBot1", bot.comandEnd)
        self.assertFalse(bot.ini)
        #with self.lock:
        thread = Thread(target=bot.iniBot)      #Activem el bot
        thread.start()
        bot.notify("mec")       #Indiquem al bot que hem escrit algo pel chat
        time.sleep(2)          #Esperem resposta del bot
        self.assertTrue(self.comprovarChat("<insultBot1>", bot.insults))    #Comprovem si ens ha insultat
        bot.ini = False
        thread.join()

    #Comrpovem el oracleBot
    def test_chatBot(self):
        print("test_chatBot")
        bot = oracleBot("chatBot1","#chatBot1","#endChatBot1")
        self.assertEqual("chatBot1", bot.name)
        self.assertEqual("#chatBot1", bot.comandActive)
        self.assertEqual("#endChatBot1", bot.comandEnd)
        self.assertFalse(bot.ini)
        #with self.lock:
        thread = Thread(target=bot.iniBot)      #Activem el bot
        thread.start()
        bot.notify("Hello bot")         #Escribim algo pel chat
        time.sleep(4)
        self.assertTrue(self.comprovarChat("<chatBot1>", ["..."]))    #Esperem resposta del chatBot
        bot.ini = False
        thread.join()

    #Comrpovem el oracleBot
    def test_tntBot(self):
        print("test_tntBot")
        bot = tntBot("tntBot1","#tntBot1","#endTntBot1",20, 4)
        self.assertEqual("tntBot1", bot.name)
        self.assertEqual("#tntBot1", bot.comandActive)
        self.assertEqual("#endTntBot1", bot.comandEnd)
        self.assertEqual(20, bot.duration)
        self.assertEqual(4, bot.lvl)
        self.assertFalse(bot.ini)
        thread = Thread(target=bot.iniBot)      #Activem el bot
        thread.start()
        bot.ini = False
        time.sleep(3)
        self.assertTrue(self.comprovarChat("<tntBot1>", ["Level: 4, time: 20"]))
        self.assertTrue(self.comprovarChat("<tntBot1>", ["You have 2 s to run. HAHAHAHA!!"]))
        self.assertTrue(self.comprovarChat("<tntBot1>", ["You are a looser"]))
        thread.join()

    def comprovarChat(self, bot, chat):
        with open("./AdventuresInMinecraft/Server/logs/latest.log","r") as file:
            lectChat = list(deque(file, maxlen=20))
            chatSplit = []
            for mss in lectChat:
                chatSplit = mss.split()
                chatSplit[-1] = chatSplit[-1].replace("\x1b[m","")
                text = " ".join(chatSplit[4:])
                if chatSplit[3] == bot:
                    #print(text)
                    if text in chat:
                        return True
            return False

if __name__ == "__main__":
    #Realitzem els tests en un ordre
    suite = unittest.TestSuite()
    suite.addTest(TestMan('test_insultBot'))
    suite.addTest(TestMan('test_chatBot'))
    suite.addTest(TestMan('test_tntBot'))
    
    #Executem els tests
    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print("Fin Tests Bots")
    #unittest.main()