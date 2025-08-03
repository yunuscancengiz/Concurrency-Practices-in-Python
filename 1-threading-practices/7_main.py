import threading
import queue
import time


q = queue.Queue()

def producer():
    for i in range(20):
        print(f'[PRODUCER] - produced: {i}')
        q.put(i)
        time.sleep(1)


def consumer():
    while True:
        item = q.get()
        if item is None:
            break

        print(f'[CONSUMER] - consumed: {item}')
        q.task_done()


t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()


t2.join()
q.put(None)
t1.join()


""" 
- Queue ile thread/process safe yapı

Amaç: Birden fazla thread ya da process aynı veriye erişmeye çalıştığında çakışmaların (race condition) önüne geçmek.

Queue ne sağlar?
- Thread-safe yapıdır → aynı anda birden fazla thread kullanabilir.
- FIFO mantığıyla çalışır (ilk giren ilk çıkar).
- put() → kuyruk ekler, get() → kuyruktan veri çeker.
- Otomatik olarak Lock ve Condition kullanır.


Output: 

[PRODUCER] - produced: 0
[CONSUMER] - consumed: 0
[PRODUCER] - produced: 1
[CONSUMER] - consumed: 1
[PRODUCER] - produced: 2
[CONSUMER] - consumed: 2
[PRODUCER] - produced: 3
[CONSUMER] - consumed: 3
.
.
.
[CONSUMER] - consumed: 15
[PRODUCER] - produced: 16
[CONSUMER] - consumed: 16
[PRODUCER] - produced: 17
[CONSUMER] - consumed: 17
[PRODUCER] - produced: 18
[CONSUMER] - consumed: 18
[PRODUCER] - produced: 19
[CONSUMER] - consumed: 19

"""