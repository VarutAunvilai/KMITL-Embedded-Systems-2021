import threading
import time

mutex = threading.Lock()

def forthread(name):
    for i in range(5):
        print(name)



for i in range(4):
    thread1 = threading.Thread(target=forthread, args=("John",))
    thread2 = threading.Thread(target=forthread, args=("Mike",))
    thread1.start()
    thread2.start()





