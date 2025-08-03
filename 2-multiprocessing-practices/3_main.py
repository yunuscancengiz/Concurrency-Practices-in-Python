from multiprocessing import Pool
import time


def slow_task(n):
    time.sleep(0.5)
    return f'task-{n} tamamlandı.'


if __name__ == '__main__':
    with Pool(processes=5) as pool:
        futures = [pool.apply_async(func=slow_task, args=(i, )) for i in range(17)]

        for f in futures:
            print(f.get())
    
""" 
17 görev var ancak 5 processes olduğu için her seferinde 5 görev yapılır ve diğerleri sıraya alınır

Output:

task-0 tamamlandı.
task-1 tamamlandı.
task-2 tamamlandı.
task-3 tamamlandı.
task-4 tamamlandı.
task-5 tamamlandı.
task-6 tamamlandı.
task-7 tamamlandı.
task-8 tamamlandı.
task-9 tamamlandı.
task-10 tamamlandı.
task-11 tamamlandı.
task-12 tamamlandı.
task-13 tamamlandı.
task-14 tamamlandı.
task-15 tamamlandı.
task-16 tamamlandı.

"""