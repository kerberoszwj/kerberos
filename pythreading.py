import threading

lock = threading.Lock()
a = 0


def change(n):
    global a
    a = a + n
    a = a - n


def runthread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


t1 = threading.Thread(target=runthread, args=(2,))
t2 = threading.Thread(target=runthread, args=(4,))
t1.start()
t2.start()
t1.join()
t2.join()
print(a)
