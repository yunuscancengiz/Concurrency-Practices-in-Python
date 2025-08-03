from multiprocessing import Pool
import time


def square(n):
    return n * n


if __name__ == '__main__':
    numbers = [1, 2, 3, 4 , 5]

    start = time.time()

    with Pool(processes=3) as pool:
        results = pool.map(square, numbers)

    end = time.time()

    print(f'Sonuçlar: {results}')
    print(f'Run time: {end - start:.2f}s.')


""" 
Pool ile process başlatma, tamamlanmalarını bekleme ve sonuçları alma işlemlerini kolaylaştırıyoruz

output:

Sonuçlar: [1, 4, 9, 16, 25]
Run time: 0.16s.

"""