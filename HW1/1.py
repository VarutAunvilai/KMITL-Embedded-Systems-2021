import threading
import time

mutex = threading.Lock()

def forthread(name):
    mutex.acquire()
    for i in range(5):
        print(name)
    mutex.release()



for i in range(4):
    thread1 = threading.Thread(target=forthread, args=("John",))
    thread2 = threading.Thread(target=forthread, args=("Mike",))
    thread1.start()
    thread2.start()



