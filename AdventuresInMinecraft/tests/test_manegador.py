from collections import deque
import os
import sys
import time
from threading import Thread
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from MyAdventures.botManager import BotManager
from MyAdventures.tnnnntBot import tntBot
from MyAdventures.mcpi.event import ChatEvent
from MyAdventures.insultBot import insultBot
from MyAdventures.oracleBot import oracleBot

class TestMan(unittest.TestCase):

    def setUp(self):
        man = BotManager()
        man.botList = []
        man.final = False

    #Comprovem singleton del manegador
    def test_singleton(self):
        print("test_singleton")
        f = BotManager()    
        f1 = BotManager()
        self.assertIs(f, f1)

    #Comprovem que es mostrin tots els atributs (allAttributes)
    def test_showAttr(self):
        print("test_showAtrr")
        bot = insultBot("insultBot2","#insultBot2","#endInsultBot2")
        self.assertEqual("insultBot2", bot.name)
        self.assertEqual("#insultBot2", bot.comandActive)
        self.assertEqual("#endInsultBot2", bot.comandEnd)
        #with self.lock:
        bot.allAttributes()     #Comprovem que s'escrigui pel chat tots els atributs
        time.sleep(1)
        self.assertTrue(self.comprovarChat("<System>", ["Attr bot: insultBot2"]))
        self.assertTrue(self.comprovarChat("<System>", ["name : insultBot2"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandActive : #insultBot2"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandEnd : #endInsultBot2"]))
        self.assertTrue(self.comprovarChat("<System>", ["chatList : []"]))
        self.assertTrue(self.comprovarChat("<System>", ["playerId : 0"]))
        self.assertTrue(self.comprovarChat("<System>", ["ini : False"]))

    #Comrpovem que es msotrin els atributs corresponents (specificAttributes)
    def test_showSpecificAtrr(self):
        print("test_showSpecificAtrr")
        bot = oracleBot("chatBot2","#chatBot2","#endChatBot2")
        self.assertEqual("chatBot2", bot.name)
        self.assertEqual("#chatBot2", bot.comandActive)
        self.assertEqual("#endChatBot2", bot.comandEnd)
        #with self.lock:
        bot.specificAttributes(["name","comandEnd","mec"])      #Comprovem que s'escriguin els atributs indicats
        time.sleep(2)
        self.assertTrue(self.comprovarChat("<System>", ["Attr bot: chatBot2"]))
        self.assertTrue(self.comprovarChat("<System>", ["name : chatBot2"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandEnd : #endChatBot2"]))
        self.assertTrue(self.comprovarChat("<System>", ["Attribute with name (mec) doesen't exist"]))

    #Comprovem el modifcador d'atributs (modifyAttribute)
    def test_modifyAttr(self):
        print("test_modifyAttr")
        bot = insultBot("insultBot3","#insultBot3","#endInsultBot3")
        self.assertEqual("insultBot3", bot.name)
        self.assertEqual("#insultBot3", bot.comandActive)
        self.assertEqual("#endInsultBot3", bot.comandEnd)
        self.assertTrue(bot.containsAttribute("name"))
        bot.modifyAttribute("name","nameChanged")
        self.assertEqual("nameChanged", bot.name)

    #Comprovem l'inicialització del manegador
    def test_init_manegador(self):
        print("test_init_manegador")
        manM = BotManager()
        #with self.lock:
        thread = Thread(target=manM.startManaging)
        thread.start()
        time.sleep(2)
        manM.final = True
        self.assertTrue(self.comprovarChat("<System>", ["Bots active"]))
        time.sleep(1)
        self.assertTrue(self.comprovarChat("<System>", ["Bots inactive"]))
        thread.join()

    #Comprovem els buscadors d'index del manegador
    def test_search_index(self):
        print("test_search_index")
        manM = BotManager()
        manM.addBots(insultBot("insultMan","#insultMan","#endInsultMan"))
        manM.addBots(oracleBot("chatMan","#chatMan","#endChatMan"))
        manM.addBots(oracleBot("tntMan","#tntMan","#endTntMan"))
        self.assertEqual(0, manM.returnIndexName("insultMan"))
        self.assertEqual(-1, manM.returnIndexName("invented"))
        self.assertEqual(1, manM.returnIndexActive("#chatMan"))
        self.assertEqual(-1, manM.returnIndexActive("invented"))
        self.assertEqual(2, manM.returnIndexEnd("#endTntMan"))
        self.assertEqual(-1, manM.returnIndexEnd("invented"))
    
    #Comprovem el checkChat() del manegador
    def test_check_chat(self):
        print("test_check_chat")
        manM = BotManager()
        manM.addBots(insultBot("insultMan1","#insultMan1","#endInsultMan1"))
        manM.addBots(oracleBot("chatMan1","#chatMan1","#endChatMan1"))
        manM.addBots(tntBot("tntMan1","#tntMan1","#endTntMan1",30,2))
        manM.checkChat(ChatEvent.Post(2,"#insultMan1"))       #Inicialitzem bots, creem thread
        manM.checkChat(ChatEvent.Post(3,"#chatMan1"))
        time.sleep(1)       #Esperem que els threads es crein
        self.assertTrue(manM.botList[0].ini)       #Comprovem que els bots s'han iniciat i pels usuaris indicats
        self.assertTrue(manM.botList[1].ini)
        self.assertEqual(2, manM.botList[0].playerId)
        self.assertEqual(3, manM.botList[1].playerId)
        manM.checkChat(ChatEvent.Post(1,"Hola"))         #Actualitzem els chatList dels bots actius
        self.assertEqual("Hola",manM.botList[0].chatList[0])    #Comprovem el valor del chat, només s'ha de mostrar als actius
        self.assertEqual("Hola",manM.botList[1].chatList[0])
        self.assertTrue(manM.botList[2].chatList == [])
        manM.checkChat(ChatEvent.Post(1,"#endInsultMan1"))      #Parem el insultBot
        self.assertFalse(manM.botList[0].ini)       #Comprovem que el bot s'ha parat i que l'altre no
        self.assertTrue(manM.botList[1].ini)
        manM.botList[1].ini = False
    
    #Comprovem la comanda #showBots del manegador
    def test_comands_showBots(self):
        print("test_comands_showBots")
        manM = BotManager()
        manM.addBots(insultBot("insultMan2","#insultMan2","#endInsultMan2"))
        manM.addBots(oracleBot("chatMan2","#chatMan2","#endChatMan2"))
        #with self.lock:
        manM.comands("#showBots")
        time.sleep(1)
        self.assertTrue(self.comprovarChat("<System>", ["Attr bot: insultMan2"]))
        self.assertTrue(self.comprovarChat("<System>", ["name : insultMan2"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandActive : #insultMan2"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandEnd : #endInsultMan2"]))
        self.assertTrue(self.comprovarChat("<System>", ["Attr bot: chatMan2"]))
        self.assertTrue(self.comprovarChat("<System>", ["name : chatMan2"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandActive : #chatMan2"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandEnd : #endChatMan2"]))

    #Comprovem la comanda #showActiveBots del manegador
    def test_comands_showActiveBots(self):
        print("test_comands_showActiveBots")
        manM = BotManager()
        manM.addBots(insultBot("insultManErr","#insultManErr","#endInsultManErr"))
        manM.addBots(oracleBot("chatManErr","#chatManErr","#endChatManErr"))
        #with self.lock:
        manM.botList[0].ini = True
        manM.comands("#showActiveBots")     #Mostrem els bots activats
        time.sleep(1)
        self.assertTrue(self.comprovarChat("<System>", ["Attr bot: insultManErr"]))
        self.assertTrue(self.comprovarChat("<System>", ["name : insultManErr"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandActive : #insultManErr"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandEnd : #endInsultManErr"]))
        self.assertFalse(self.comprovarChat("<System>", ["Attr bot: chatManErr"]))
        self.assertFalse(self.comprovarChat("<System>", ["name : chatManErr"]))
        self.assertFalse(self.comprovarChat("<System>", ["comandActive : #chatManErr"]))
        self.assertFalse(self.comprovarChat("<System>", ["comandEnd : #endChatManErr"]))

    #Comprovem la comanda #stopBots del manegador
    def test_comands_stopBots(self):
        print("test_comands_stopBots")
        manM = BotManager()
        manM.addBots(insultBot("insultMan11","#insultMan11","#endInsultMan11"))
        manM.addBots(insultBot("insultMan22","#insultMan22","#endInsultMan22"))
        manM.addBots(oracleBot("chatMan11","#chatMan11","#endChatMan11"))
        #with self.lock:
        manM.botList[0].ini = True 
        manM.botList[1].ini = True
        manM.botList[2].ini = True
        manM.comands("#stopBots")           #Parem els bots
        self.assertFalse(manM.botList[0].ini)
        self.assertFalse(manM.botList[1].ini)
        self.assertFalse(manM.botList[2].ini)

    #Comprovem la comanda #showAttr del manegador
    def test_comands_showAttr(self):
        print("test_comands_showAttr")
        manM = BotManager()
        manM.addBots(oracleBot("chatManErr1","#chatManErr1","#endChatManErr1"))
        #with self.lock:
        manM.comands("#showAttr")           #Realitzem la petició malament
        manM.comands("#showAttr botInvented")       #Realitzem la petició amb el nom d'un bot inventat
        manM.comands("#showAttr chatManErr1")        #Mostrem els atributs del chatBot
        time.sleep(1)
        self.assertTrue(self.comprovarChat("<System>", ["Bad request (#showAttr nameBot)"]))
        self.assertTrue(self.comprovarChat("<System>", ["Doesn't exist a bot with name: botInvented"]))
        self.assertTrue(self.comprovarChat("<System>", ["Attr bot: chatManErr1"]))
        self.assertTrue(self.comprovarChat("<System>", ["name : chatManErr1"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandActive : #chatManErr1"]))
        self.assertTrue(self.comprovarChat("<System>", ["comandEnd : #endChatManErr1"]))
        self.assertTrue(self.comprovarChat("<System>", ["chatList : []"]))
        self.assertTrue(self.comprovarChat("<System>", ["playerId : 0"]))
        self.assertTrue(self.comprovarChat("<System>", ["ini : False"]))

    #Comprovem la comanda #showSpecificAttr del manegador
    def test_comands_showSpecificAttr(self):
        print("test_comands_showSpecificAttr")
        manM = BotManager()
        manM.addBots(oracleBot("chatManErr2","#chatManErr2","#endChatManErr2"))
        #with self.lock:
        manM.botList[0].chatList = ["Hola"]
        manM.comands("#showSpecificAttr")           #Realitzem la petició malament
        manM.comands("#showSpecificAttr botInvented name")       #Realitzem la petició amb el nom d'un bot inventat
        manM.comands("#showSpecificAttr chatManErr2 name playerId chatList ini mec")        #Mostrem els atributs del chatBot
        time.sleep(1)
        self.assertTrue(self.comprovarChat("<System>", ["Bad request (#showSpecificAttr nameBot att1 attr2 ...)"]))
        self.assertTrue(self.comprovarChat("<System>", ["Doesn't exist a bot with name: botInvented"]))
        self.assertTrue(self.comprovarChat("<System>", ["Attr bot: chatManErr1"]))
        self.assertTrue(self.comprovarChat("<System>", ["name : chatManErr1"]))
        self.assertTrue(self.comprovarChat("<System>", ["chatList : ['Hola']"]))
        self.assertTrue(self.comprovarChat("<System>", ["playerId : 0"]))
        self.assertTrue(self.comprovarChat("<System>", ["ini : False"]))
        self.assertTrue(self.comprovarChat("<System>", ["Attribute with name (mec) doesen't exist"]))

    #Comprovem la comanda #modifyAttribute del manegador
    def test_comands_modifyAttribute(self):
        print("test_comands_modifyAttribute")
        manA = BotManager() 
        manA.addBots(tntBot("tntManErr","#tntManErr","#endTntManErr",10, 1))
        #self.assertEqual("tntManErr", manA.botList[0].name)
        self.assertEqual("#tntManErr", manA.botList[0].comandActive)        #Comprovem valors inicials
        self.assertEqual("#endTntManErr", manA.botList[0].comandEnd)
        self.assertEqual(10 , manA.botList[0].duration)
        self.assertEqual(1, manA.botList[0].lvl)
        manA.comands("#modifyAttribute mec mec")                #Modifiquem valors
        manA.comands("#modifyAttribute invMan name troll")
        manA.comands("#modifyAttribute tntManErr mec 30")
        manA.comands("#modifyAttribute tntManErr lvl 20")
        self.assertEqual(4, manA.botList[0].lvl)                #Comprovem nous valors per codi
        manA.comands("#modifyAttribute tntManErr lvl -20")
        self.assertEqual(1, manA.botList[0].lvl)
        manA.comands("#modifyAttribute tntManErr name botTnt")
        self.assertEqual("botTnt", manA.botList[0].name)
        time.sleep(1)                                           #Comprovem nous valors pel chat
        self.assertTrue(self.comprovarChat("<System>", ["Bad request (#modifyAttribute nameBot attributeSelected newValue)"]))
        self.assertTrue(self.comprovarChat("<System>", ["Doesn't exist a bot with that name: invMan"]))
        self.assertTrue(self.comprovarChat("<System>", ["Doesn't exist an attribute named: mec"]))
        self.assertTrue(self.comprovarChat("<System>", ["You have modified: lvl His new value is: 4"]))
        self.assertTrue(self.comprovarChat("<System>", ["You have modified: lvl His new value is: 1"]))
        self.assertTrue(self.comprovarChat("<System>", ["You have modified: name His new value is: botTnt"]))

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
    suite.addTest(TestMan('test_singleton'))
    suite.addTest(TestMan('test_showAttr'))
    suite.addTest(TestMan('test_showSpecificAtrr'))
    suite.addTest(TestMan('test_modifyAttr'))
    suite.addTest(TestMan('test_init_manegador'))
    suite.addTest(TestMan('test_search_index'))
    suite.addTest(TestMan('test_check_chat'))
    suite.addTest(TestMan('test_comands_showBots'))
    suite.addTest(TestMan('test_comands_showActiveBots'))
    suite.addTest(TestMan('test_comands_stopBots'))
    suite.addTest(TestMan('test_comands_showAttr'))
    suite.addTest(TestMan('test_comands_showSpecificAttr'))
    suite.addTest(TestMan('test_comands_modifyAttribute'))
    
    #Executem els tests
    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print("Fin Tests Manegador")
    #unittest.main()
    