import Pyro4
from threading import Thread
from botInitialization import botInitialization

@Pyro4.expose
class serverMinecraft(object):
    def run_executable(self):
        bot = botInitialization()
        thread = Thread(target=bot.initialization)
        thread.start()

    #def run_server(self, ip):        
daemon = Pyro4.Daemon(host="192.168.1.126")
uri = daemon.register(serverMinecraft)
print(f"Ready. Object URI = {uri}")
daemon.requestLoop()