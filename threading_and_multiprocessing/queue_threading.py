# from queue import Queue

# q = Queue()
# q.put(1) 
# q.put(2) 
# q.put(3) 

# first = q.get() 
# print(first) 

from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get() 
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True   #daemon is a background thread if it dies the main thread dies
        t.start()
    for x in range(20):
        q.put(x)

    q.join()  

    print('main done')
