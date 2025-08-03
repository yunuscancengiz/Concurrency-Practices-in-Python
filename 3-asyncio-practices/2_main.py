import asyncio

async def task(name):
    print(f"{name} başlıyor")
    await asyncio.sleep(1)
    print(f"{name} bitiyor")

async def main():
    await asyncio.gather(*[task(f"Görev-{i}") for i in range(5)])

asyncio.run(main())


""" 
threading ile karşılaştırma


import threading
import time

def task(name):
    print(f"{name} başlıyor")
    time.sleep(1)
    print(f"{name} bitiyor")

for i in range(5):
    t = threading.Thread(target=task, args=(f"Görev-{i}",))
    t.start()

    

Her iki kod da aynı anda 5 işi başlatır ama:
- threading → 5 gerçek thread açar
- asyncio → 1 thread içinde 5 coroutine çalıştırır (çok daha hafiftir)


Ne Zaman asyncio Kullanmalıyım:
    Kullan:
        - API çağrısı (HTTP client)
        - Veritabanı sorgusu (async destekli)
        - Gerçek zamanlı socket bağlantıları (chat, oyun)
        - Dosya okuma/yazma (async destekli kütüphanelerle)

    Kullanma:
        - CPU yoğun iş (hesaplama, görüntü işleme vs.)
            → async içinde CPU-bound kod kullanırsan event loop’u kilitlersin.
"""