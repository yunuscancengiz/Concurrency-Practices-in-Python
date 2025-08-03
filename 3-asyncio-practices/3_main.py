import asyncio
import random


async def download(url):
    print(f'{url} - downloading...')
    await asyncio.sleep(random.uniform(0.5, 1.5))
    print(f'{url} - downloaded.')
    return f'{url} - content'


async def main():
    urls = [f'https://example.com/product/{i}' for i in range(10)]

    # start all tasks
    tasks = [download(url=url) for url in urls]

    # run all of them asyncronusly
    results = await asyncio.gather(*tasks)

    print('\nSonuçlar')
    for res in results:
        print(res)
    
asyncio.run(main=main())