from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def task(n):
    time.sleep(1)
    return f'task-{n} tamamlandı.'


with ThreadPoolExecutor(max_workers=7) as executor:
    futures = [executor.submit(task, i) for i in range(1, 26)]

    for future in as_completed(futures):
        print('->', future.result())