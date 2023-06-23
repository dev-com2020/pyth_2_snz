from multiprocessing import Process
import os


def process_info():
    print('proces id:', os.getpid())


def worker(number):
    print(f'Worker number {number}')
    process_info()


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=worker, args=(i,))
        p.start()
