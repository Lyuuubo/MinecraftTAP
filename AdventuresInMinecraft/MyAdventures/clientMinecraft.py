import Pyro4
remote_executor = Pyro4.Proxy("PYRO:obj_4070561aac9f4e15b8f5b99969f1fed7@192.168.1.126:55888")
result = remote_executor.run_executable()
print(result)