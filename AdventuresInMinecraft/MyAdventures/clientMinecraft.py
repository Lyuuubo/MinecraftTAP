import Pyro4
remote_executor = Pyro4.Proxy("PYRO:obj_300c1407b1d3473d9883827113c77c34@192.168.1.126:56695")
result = remote_executor.run_executable()
print(result)