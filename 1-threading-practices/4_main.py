import threading


lock = threading.Lock()
counter = 0     # shared resource
def increase():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1
            if counter % 500 == 0:
                print(f"[{threading.current_thread().name}] counter: {counter}")


threads = []
for _ in range(25):
    t = threading.Thread(target=increase)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Sonuç: {counter}')