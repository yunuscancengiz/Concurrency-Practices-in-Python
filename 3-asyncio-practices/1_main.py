import asyncio


async def say_hello(name):
    print(f'hello, {name}!')
    await asyncio.sleep(1)
    print(f'good bye, {name}...')


async def main():
    await asyncio.gather(
        say_hello(name='Mathilda'),
        say_hello(name='Pixel'),
        say_hello(name='Gofret')
    )

asyncio.run(main())




""" 
| Özellik            | `threading`          | `multiprocessing`         | `asyncio`                     |
| ------------------ | -------------------- | ------------------------- | ----------------------------- |
| Eşzamanlılık tipi  | Gerçek zamanlı       | Gerçek paralellik         | Tek iş parçacığında eşzamanlı |
| Uygun olduğu işler | I/O-bound            | CPU-bound                 | I/O-bound                     |
| GIL etkisi         | Var                  | Yok                       | GIL'den etkilenmez            |
| Hafiflik           | Orta                 | Ağır                      | Çok hafif                     |
| Kullanım maliyeti  | Kolay                | Orta                      | Başta zor, sonra çok güçlü    |
| Örnek kullanım     | Web scraping, socket | Görüntü işleme, hesaplama | Web sunucuları, API çağrıları |


"""