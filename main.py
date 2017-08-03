from multiprocessing import Process, Manager
import new
import always

Process(target=new).start()
Process(target=always).start()