import threading
import time
import queue
import random


url_queue = queue.Queue()

def fetch_url():
    while True:
        url = url_queue.get()
        if url is None:
            break

        print(f'[{threading.current_thread().name}] - {url} processing...')
        time.sleep(random.uniform(0.5, 1.5))
        print(f'[{threading.current_thread().name}] - {url} processed.')

        url_queue.task_done()
    

if __name__ == '__main__':
    urls = [f'https://example.com/product/{i}' for i in range(10)]
    for url in urls:
        url_queue.put(url)

    num_workers = 3
    threads = []

    for i in range(num_workers):
        t = threading.Thread(target=fetch_url, name=f'Worker-{i}')
        t.start()
        threads.append(t)

    url_queue.join()

    # send sentinel to stop threads
    for _ in range(num_workers):
        url_queue.put(None)

    for t in threads:
        t.join()
    
    print('All urls have been processed!')

    