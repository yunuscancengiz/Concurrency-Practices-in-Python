import threading
import time


def worker(task_id):
    print(f'Thread-{task_id} başladı')
    time.sleep(2)
    print(f'Thread-{task_id} bitti')


threads = []
for i in range(10):
    t = threading.Thread(target=worker, args=(i, ))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

print('tüm işlemler bitti.')


""" 
Output:

Thread-0 başladı
Thread-1 başladı
Thread-2 başladı
Thread-3 başladı
Thread-4 başladı
Thread-5 başladı
Thread-6 başladı
Thread-7 başladı
Thread-8 başladı
Thread-9 başladı
Thread-0 bitti
Thread-2 bitti
Thread-3 bitti
Thread-1 bitti
Thread-4 bitti
Thread-8 bitti
Thread-5 bitti
Thread-7 bitti
Thread-6 bitti
Thread-9 bitti
tüm işlemler bitti.
"""