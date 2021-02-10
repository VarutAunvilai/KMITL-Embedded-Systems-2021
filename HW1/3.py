import threading
import time
import queue

queue = queue.Queue()

def forqueue():
    while True:
        number = queue.get()
        print(number)
        queue.task_done()




for i in range(20):
    queue.put(i)

thread1 = threading.Thread(target=forqueue, args=())
thread1.start()


