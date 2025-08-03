import threading


def print_numbers(nums):
    for i in nums:
        print(f'Thread: {i}')


thread_nums = [num for num in range(20, 51)]
main_nums = [num for num in range(20)]


# thread oluştur
t = threading.Thread(target=print_numbers, args=(thread_nums, ))

# başlat
t.start()

# main thread'de aynı fonksiyonu farklı liste ile çağır
print_numbers(nums=main_nums)

# main thread devam eder
print('main thread devam ediyor...')

# tüm thread'lerin bitmesini bekle
t.join()

print('tüm işlemler bitti.')


"""
Output:

Thread: 20
Thread: 21
Thread: 22
Thread: 23
Thread: 24
Thread: 25
Thread: 26
Thread: 27
Thread: 28
Thread: 29
Thread: 0
Thread: 1
Thread: 2
Thread: 3
Thread: 4
Thread: 5
Thread: 6
Thread: 7
Thread: 8
Thread: 9
Thread: 10
Thread: 11
Thread: 12
Thread: 13
Thread: 30
Thread: 31
Thread: 32
Thread: 33
Thread: 34
Thread: 14
Thread: 35
Thread: 15
Thread: 16
Thread: 17
Thread: 36
Thread: 18
Thread: 19
Thread: 37
main thread devam ediyor...
Thread: 38
Thread: 39
Thread: 40
Thread: 41
Thread: 42
Thread: 43
Thread: 44
Thread: 45
Thread: 46
Thread: 47
Thread: 48
Thread: 49
Thread: 50
tüm işlemler bitti.
"""
