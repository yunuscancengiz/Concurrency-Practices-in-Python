from multiprocessing import Process
import time


def cpu_task():
    count = 0
    for _ in range(10 ** 7):
        count += 1


if __name__ == '__main__':
    start = time.time()

    processes = []
    for _ in range(4):
        p = Process(target=cpu_task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()

    print(f'Multiprocessing run time: {end - start:.2f}s.')


"""
Aynı işlemi aşağıdaki threading kodu ile yapınca run time 1.59 saniye olurken multiprocessing ile 0.61 saniye


import threading
import time

def cpu_task():
    count = 0
    for _ in range(10**7):
        count += 1
    return count

start = time.time()

threads = []
for _ in range(4):
    t = threading.Thread(target=cpu_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print(f"Multithreading süresi: {end - start:.2f} saniye")


"""


""" 
Ne zaman threading ne zaman multiprocessing?


🎯 1. I/O-bound ve CPU-bound Nedir?
Tür	        |   Ne Demek?	                                            |       Örnek
I/O-bound   |	Programın çoğu zamanı I/O işlemi bekleyerek geçiyor     |	    Dosya okuma/yazma, API istekleri, veri tabanı sorgusu
CPU-bound	|   Programın çoğu zamanı işlemci kullanıyor	            |       Sayı asal mı kontrol et, büyük veri işle, resim işleme


🎯 Özetle:
                        Multithreading      |	Multiprocessing
GIL etkisi	            Evet (sınırlar)	    |       Hayır
I/O-bound için uygun	    ✅	           |    ❌ Overkill
CPU-bound için uygun	    ❌	           |        ✅
Hafiflik	                Hafif           |	Ağır (her biri ayrı process)
Kullanım zorluğu        	Kolay	        |       Orta
"""