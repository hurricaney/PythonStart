# condition锁

# 生产者仅仅在仓库未满的时候生产，仓库满则停止生产
# 消费者仅仅在仓库有产品的时候才能消费，仓空则等待
# 当消费者发现仓库没有产品时候通知生产者生产
# 生产者在生产出可消费产品的时候，应该通知等待的消费者去消费

# 生产1S，消费4S，仓库容量10

import threading
import time

products=[]
condition=threading.Condition()

class Consumer(threading.Thread):
    def consume(self):
        global condition
        global products
        condition.acquire()
        if len(products) ==0:
            condition.wait()
            print("消费者提醒：没有产品去消费了")
        products.pop()
        print("消费者提醒：消费1个产品")
        print("消费者提醒：当前库存的产品数为"+str(len(products)))
        condition.notify()#通知
        condition.release()#解锁
    def run(self):
        for i in range(0,20):
            time.sleep(4)#消费一个产品的时间4s
            self.consume()

class Producer(threading.Thread):
    def produce(self):
        global condition
        global products
        condition.acquire()#设置条件锁
        if len(products)==10:
            condition.wait()#等待
            print("生产者提醒：生产的产品数为："+str(len(products)))
            print("生产者提醒：停止生产！")
        products.append(1)
        print("生产者提醒：产品总数为："+str(len(products)))
        condition.notify()#通知
        condition.release()#解锁
    def run(self):
        for i in range(0,20):
            time.sleep(1)#生产一个产品的时间1s
            self.produce()

producer=Producer()#生产者实例
consumer=Consumer()#消费者实例
producer.start()
consumer.start()
producer.join()
consumer.join()
