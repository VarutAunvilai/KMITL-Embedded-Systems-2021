import threading
import time

def forqueue(number):
    print(number)



for i in range(20):
    thread1 = threading.Thread(target=forqueue, args=(i,))
    thread1.start()


