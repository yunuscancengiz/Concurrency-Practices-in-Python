from multiprocessing import Process, Queue
import time


def producer(q: Queue):
    for i in range(10):
        print(f'[PRODUCER] - producer: {i}')
        q.put(i)
        time.sleep(1)
    q.put(None)     # exit signal


def consumer(q: Queue):
    while True:
        item = q.get()
        if item is None:
            break

        print(f'[CONSUMER] - consumed: {item}')


if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=consumer, args=(q, ))
    p2 = Process(target=producer, args=(q, ))

    p1.start()
    p2.start()

    p2.join()
    p1.join()

    print('DONE')


""" 
Output: 

[PRODUCER] - producer: 0
[CONSUMER] - consumed: 0
[PRODUCER] - producer: 1
[CONSUMER] - consumed: 1
[PRODUCER] - producer: 2
[CONSUMER] - consumed: 2
[PRODUCER] - producer: 3
[CONSUMER] - consumed: 3
[PRODUCER] - producer: 4
[CONSUMER] - consumed: 4
[PRODUCER] - producer: 5
[CONSUMER] - consumed: 5
[PRODUCER] - producer: 6
[CONSUMER] - consumed: 6
[PRODUCER] - producer: 7
[CONSUMER] - consumed: 7
[PRODUCER] - producer: 8
[CONSUMER] - consumed: 8
[PRODUCER] - producer: 9
[CONSUMER] - consumed: 9
DONE

"""