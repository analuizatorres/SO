import threading
import time
import random

semaforo = threading.Semaphore(3)

def caixa(i):
    semaforo.acquire()
    time.sleep(random.randint(3,10))
    print(f"Cliente {i} Atendido :D")
    semaforo.release()

if __name__=="__main__":
    for i in range(30):
        t1 = threading.Thread(target=caixa, args=(i,))
        t1.start()
