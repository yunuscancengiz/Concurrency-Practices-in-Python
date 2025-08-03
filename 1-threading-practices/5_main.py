from concurrent.futures import ThreadPoolExecutor
import time


def download_file(filename):
    print(f'[{filename}] indiriliyor...')
    time.sleep(2)
    print(f'[{filename}] imdirildi.')
    return f'{filename} sonucu'


# threadpool oluşturur
with ThreadPoolExecutor(max_workers=4) as executor:
    filenames = [f'file{i}' for i in range(1, 11)]

    # tüm görevleri sırayla kuyruğa atar
    results = executor.map(download_file, filenames)
    
    for result in results:
        print('->', result)

# executor_map kullanılınca sonuçlar görev sırasına göre döner
# eğer tamamlanma sırasına göre dönmesini istersek submit() ve as_completed() kullanmalıyız
# örneği 6_main.py'da


""" 
Output: 

[file1] indiriliyor...
[file2] indiriliyor...
[file3] indiriliyor...
[file4] indiriliyor...
[file1] imdirildi.
[file5] indiriliyor...
-> file1 sonucu
[file3] imdirildi.
[file4] imdirildi.
[file7] indiriliyor...
[file2] imdirildi.
[file6] indiriliyor...
[file8] indiriliyor...
-> file2 sonucu
-> file3 sonucu
-> file4 sonucu
[file5] imdirildi.
[file9] indiriliyor...
-> file5 sonucu
[file7] imdirildi.
[file6] imdirildi.
[file10] indiriliyor...
-> file6 sonucu
-> file7 sonucu
[file8] imdirildi.
-> file8 sonucu
[file9] imdirildi.
-> file9 sonucu
[file10] imdirildi.
-> file10 sonucu

"""