from multiprocessing import Process, Manager
import new
import always
import post

Process(target=new).start()
Process(target=always).start()
Process(target=post).start()