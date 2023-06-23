import asyncio
import time


# async def main():
#     print('Hello..')
#     await asyncio.sleep(1)
#     print('...World')
#     await asyncio.sleep(2)
#     print('...again :)')
#
#
# asyncio.run(main())

# def count():
#     print("1")
#     time.sleep(1)
#     print('2')
#
# def main():
#     count()
#     count()
#     count()
#
# if __name__ == '__main__':
#     s = time.perf_counter()
#     main()
#     elapsed = time.perf_counter() - s
#     print(f"Completed in {elapsed:0.2f} sec.")


async def count():
    print("1")
    await asyncio.sleep(1)
    print('2')


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} sec.")
