import threading
import time

semaphore = threading.Semaphore(2)

def forsemaphore(name):
    semaphore.acquire()
    for i in range(5):
        print(name)
        time.sleep(0.5)
    semaphore.release()



for i in range(2):
    thread1 = threading.Thread(target=forsemaphore, args=("John",))
    thread2 = threading.Thread(target=forsemaphore, args=("Mike",))
    thread3 = threading.Thread(target=forsemaphore, args=("Sam",))
    thread1.start()
    thread2.start()
    thread3.start()

