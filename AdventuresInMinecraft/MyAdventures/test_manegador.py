from collections import deque
import time
from threading import Thread, Lock
import unittest

from botManager import BotManager
from insultBot import insultBot
from oracleBot import oracleBot

class TestMan(unittest.TestCase):
    lock: Lock = Lock()

    def test_singleton(self):
        print("test_singleton")
        f = BotManager()    
        f1 = BotManager()
        self.assertIs(f, f1)

    def test_insultBot(self):
        print("test_insultBot")
        man = BotManager()
        bot = insultBot("insultBot1","#insultBot1","#endInsultBot1")
        self.assertEqual("insultBot1", bot.name)
        self.assertEqual("#insultBot1", bot.comandActive)
        self.assertEqual("#endInsultBot1", bot.comandEnd)
        self.assertFalse(bot.ini)
        with self.lock:
            thread = Thread(target=bot.iniBot)
            thread.start()
            bot.notify("mec")
            time.sleep(2)
            self.assertTrue(self.comprovarChat("<insultBot1>", bot.insults))
            bot.ini = False

    def test_chatBot(self):
        print("test_chatBot")
        man = BotManager()
        bot = oracleBot("chatBot1","#chatBot1","#endChatBot1")
        self.assertEqual("chatBot1", bot.name)
        self.assertEqual("#chatBot1", bot.comandActive)
        self.assertEqual("#endChatBot1", bot.comandEnd)
        self.assertFalse(bot.ini)
        with self.lock:
            thread = Thread(target=bot.iniBot)
            thread.start()
            bot.notify("Hello bot")
            time.sleep(2)
            self.assertTrue(self.comprovarChat("<chatBot1>", "..."))
            bot.ini = False
    
    def test_showAttr(self):
        print("test_showAtrr")
        bot = insultBot("insultBot2","#insultBot2","#endInsultBot2")
        self.assertEqual("insultBot2", bot.name)
        self.assertEqual("#insultBot2", bot.comandActive)
        self.assertEqual("#endInsultBot2", bot.comandEnd)
        with self.lock:
            bot.allAttributes()
            time.sleep(2)
            self.assertTrue(self.comprovarChat("<System>", "Attr bot: insultBot2"))
            self.assertTrue(self.comprovarChat("<System>", "name : insultBot2"))
            self.assertTrue(self.comprovarChat("<System>", "comandActive : #insultBot2"))
            self.assertTrue(self.comprovarChat("<System>", "comandEnd : #endInsultBot2"))
            self.assertTrue(self.comprovarChat("<System>", "chatList : []"))
            self.assertTrue(self.comprovarChat("<System>", "playerId : 0"))
            self.assertTrue(self.comprovarChat("<System>", "ini : False"))
            bot.ini = False

    def test_showSpecificAtrr(self):
        print("test_showSpecificAtrr")
        bot = oracleBot("chatBot2","#chatBot2","#endChatBot2")
        self.assertEqual("chatBot2", bot.name)
        self.assertEqual("#chatBot2", bot.comandActive)
        self.assertEqual("#endChatBot2", bot.comandEnd)
        with self.lock:
            bot.specificAttributes(["name","comandEnd","mec"])
            time.sleep(2)
            self.assertTrue(self.comprovarChat("<System>", "Attr bot: chatBot2"))
            self.assertTrue(self.comprovarChat("<System>", "name : chatBot2"))
            self.assertTrue(self.comprovarChat("<System>", "comandEnd : #endChatBot2"))
            self.assertTrue(self.comprovarChat("<System>", "Attribute with name (mec) doesen't exist"))
            bot.ini = False
        
    def test_modifyAttr(self):
        print("test_modifyAttr")
        bot = oracleBot("insultBot3","#insultBot3","#endInsultBot3")
        self.assertEqual("insultBot3", bot.name)
        self.assertEqual("#insultBot3", bot.comandActive)
        self.assertEqual("#endInsultBot3", bot.comandEnd)
        self.assertTrue(bot.containsAttribute("name"))
        bot.modifyAttribute("name","nameChanged")
        self.assertEqual("nameChanged", bot.name)

    def comprovarChat(self, bot, chat):
        with open("./AdventuresInMinecraft/Server/logs/latest.log","r") as file:
            lectChat = list(deque(file, maxlen=10))
            chatSplit = []
            for mss in lectChat:
                chatSplit = mss.split()
                chatSplit[-1] = chatSplit[-1].replace("\x1b[m","")
                text = " ".join(chatSplit[4:])
                if chatSplit[3] == bot:
                    if text in chat:
                        return True
            return False

if __name__ == "__main__":
    # Usando TestLoader para cargar los test en orden específico
    suite = unittest.TestSuite()
    suite.addTest(TestMan('test_singleton'))
    suite.addTest(TestMan('test_insultBot'))
    suite.addTest(TestMan('test_chatBot'))
    suite.addTest(TestMan('test_showAttr'))
    suite.addTest(TestMan('test_showSpecificAtrr'))
    suite.addTest(TestMan('test_modifyAttr'))
    
    # Ejecutar la suite de pruebas
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #unittest.main()
    