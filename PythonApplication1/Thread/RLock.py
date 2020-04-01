# Rlock锁
import threading
import logging
# logging.basicConfig(level=logging.DEBUG)

class  mythread(threading.Thread):
    def run(self):
        global x
        lock.acquire()
        x=x+10
        logging.info('list1:%d',x)
        print('%s:%d'%(self.name,x))
        lock.release()

x=0
lock=threading.RLock()
list1=[]
for i in range(5):
    list1.append(mythread())

for i in list1:
    i.start()

