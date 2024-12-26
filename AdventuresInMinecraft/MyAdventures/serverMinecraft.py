import Pyro5.api
# from threading import Thread
# from botInitialization import botInitialization

@Pyro5.api.expose
class serverMinecraft(object):
    def run_executable(self, message):
        #bot = botInitialization()
        #thread = Thread(target=bot.initialization)
        #thread.start()
        print(message)
        return "perro"

    #def run_server(self, ip):        
daemon = Pyro5.api.Daemon(host="192.168.154.37")
ns = Pyro5.api.locate_ns(host="192.168.154.37", port=9090)
uri = daemon.register(serverMinecraft)
ns.register("ServerMinecraft", uri)
print(f"Ready. Object URI = {uri}")
daemon.requestLoop()