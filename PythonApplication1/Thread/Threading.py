import time
import threading

def test():
    time.sleep(2)
    for i in range(10):
        print('打印：'+str(i))

thread1=threading.Thread(target=test)
print('1.当前线程是否是活动的：',thread1.isAlive())
thread1.start()

print('2.当前线程是否是活动的：',thread1.isAlive())
print('3.当前线程是：',thread1.getName())
thread1.join()
print('4.线程完毕！！！')