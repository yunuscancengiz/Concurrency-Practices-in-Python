from multiprocessing import Pool
import time


def is_prime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    numbers = list(range(10000, 10200))

    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(is_prime, numbers)
    end = time.time()

    for num, res in zip(numbers, results):
        if res:
            print(f'{num} -> Asal')
    print(f'\nrun time: {end - start:.2f}s.')


""" 
bir büyük sayı listesindeki sayıların asal olup olmama durumlarını multiprocessing ile kontrol eder

Output:

10007 -> Asal
10009 -> Asal
10037 -> Asal
10039 -> Asal
10061 -> Asal
10067 -> Asal
10069 -> Asal
10079 -> Asal
10091 -> Asal
10093 -> Asal
10099 -> Asal
10103 -> Asal
10111 -> Asal
10133 -> Asal
10139 -> Asal
10141 -> Asal
10151 -> Asal
10159 -> Asal
10163 -> Asal
10169 -> Asal
10177 -> Asal
10181 -> Asal
10193 -> Asal

run time: 0.16s.
"""