import Pyro5.api

ns = Pyro5.api.locate_ns(host="192.168.154.37", port=9090)
uri = ns.lookup("ServerMinecraft")
remote_executor = Pyro5.api.Proxy(uri)
result = remote_executor.run_executable("miau")
print(result)