import threading


def print_numbers():
    for i in range(5):
        print(f'Thread: {i}')


# thread oluştur
t = threading.Thread(target=print_numbers)

# başlat
t.start()

# main thread devam eder
print('main thread devam ediyor...')

# tüm thread'lerin bitmesini bekle
t.join()

print('tüm işlemler bitti.')


"""
Output:

Thread: 0
Thread: 1
Thread: 2
main thread devam ediyor...
Thread: 3
Thread: 4
tüm işlemler bitti.
"""
